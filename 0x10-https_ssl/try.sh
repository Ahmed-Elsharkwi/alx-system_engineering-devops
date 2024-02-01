#!/user/bin/env bash
dig geeksforgeeks.org +noall +answer | awk '{print $NF}'
