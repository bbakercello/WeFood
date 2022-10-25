import Head from 'next/head'
import Image from 'next/image'
import styles from '../styles/Home.module.css'
import Link from 'next'
export default function Home() {
  return (
    <div className={styles.container}>
      <h1 className='bg-sky-600'>My List</h1>
      <div>
        <h4><Link></Link></h4>
      </div>
    </div>
  )
}
