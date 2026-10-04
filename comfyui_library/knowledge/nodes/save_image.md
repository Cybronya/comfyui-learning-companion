# SaveImage

## 节点类型

`SaveImage`

## 分类

Output

## 作用

`SaveImage` 负责将生成完成的图片保存到 ComfyUI 输出目录。

它是 workflow 的最终输出节点。

---

## Workflow 位置

```text
VAEDecode

     ↓

IMAGE

     ↓

SaveImage

     ↓

Output File
```

---

## 输入

### images

来自：

```text
VAEDecode
```

---

### filename_prefix

文件名前缀。

例如：

```text
ComfyUI
```

生成：

```text
ComfyUI_00001.png
```

---

## 输出

保存后的图片文件。

默认位置：

```text
ComfyUI/output/
```

---

## 初学者理解

`SaveImage` 就像：

> 完成绘画后，把作品保存到文件夹。

它本身不会改变图片质量。

---

## 为什么它重要？

虽然它是简单节点，但是它标志着：

```text
AI生成过程

↓

人类可见结果
```

---

## 常见错误

### 忘记连接 SaveImage

结果：

* 图片生成了
* 但是没有保存

---

### 文件名冲突

可能导致：

* 图片管理混乱

---

## 学习任务

实验：

修改：

```text
filename_prefix
```

例如：

```text
test_sd15
```

生成多张图片。

观察：

文件命名规则。

学习目标：

理解 workflow 输出管理。
