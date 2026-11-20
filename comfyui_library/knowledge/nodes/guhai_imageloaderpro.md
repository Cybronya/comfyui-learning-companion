# GuHai_ImageLoaderPro

## 节点类型

`GuHai_ImageLoaderPro`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `文件夹路径:STRING`（1 次）
- `起始索引:INT`（1 次）
- `加载模式:COMBO`（1 次）
- `保留透明通道:BOOLEAN`（1 次）
- `包含子文件夹:BOOLEAN`（1 次）
- `显示扩展名:BOOLEAN`（1 次）
- `自定义扩展名:STRING`（1 次）
- `重置递增:BOOLEAN`（1 次）

## 输出

- `图像:IMAGE`（1 次）
- `文件名:STRING`（1 次）
- `图像路径:STRING`（1 次）
- `扩展名:STRING`（1 次）
- `路径+文件名:STRING`（1 次）
- `序号:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", 0, "单张模式", false, false, true, "", false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
