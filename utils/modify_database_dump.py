import argparse
import re
import sys


def parse_args():
    parser = argparse.ArgumentParser(description='Modify Wordpress database dump.')
    parser.add_argument(
        '--old-url',
        type=str,
        help='the old URL e.g. http://www.oldurl.com',
        required=True
    )
    parser.add_argument(
        '--new-url',
        type=str,
        default='http://localhost:8000',
        help='the new URL e.g. http://www.newurl.com',
    )

    return parser.parse_args()


def main():
    args = parse_args()

    # Find out what the options, postmeta and posts tables are called from the
    # database dump.
    table_names = {}
    table_mappings = {
        'wp_options' : 'options',
        'wp_postmeta': 'postmeta',
        'wp_posts': 'posts'
    }
    for line in sys.stdin:
        if line.startswith('CREATE TABLE'):
            table_name = line.split('`')[1]
            for k, v in table_mappings.iteritems():
                if table_name.endswith(v):
                    table_names[k] = table_name
        print(line)

    change = (args.old_url, args.new_url)

    print("-- Added by %s" % sys.argv[0])

    print("UPDATE wp_options SET option_value = replace(option_value, '%s', '%s') WHERE option_name = 'home' OR option_name = 'siteurl';" % change)

    print("UPDATE wp_posts SET guid = replace(guid, '%s', '%s');" % change)

    print("UPDATE wp_posts SET post_content = replace(post_content, '%s', '%s');" % change)

    print("UPDATE wp_postmeta SET meta_value = replace(meta_value, '%s', '%s');" % change)


if __name__ == '__main__':
    main()
