
rm -rf build
rm cython_eigenx.c*
python setup.py build_ext --inplace
cp -fv cython_eigenx.cpython-310-darwin.so ~/virtenv/py3105env/lib/python3.10/site-packages
