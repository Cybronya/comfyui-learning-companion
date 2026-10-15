# DapaoSafeSaveImage

## 节点类型

`DapaoSafeSaveImage`

## 分类

Output

## 作用

输出类节点：把结果写到磁盘（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `🖼️ 图像:IMAGE`（1 次）
- `📄 文件名前缀:STRING`（1 次）
- `💾 格式:COMBO`（1 次）
- `📉 质量:INT`（1 次）
- `😶‍🌫️ 移除元数据:BOOLEAN`（1 次）
- `📂 自定义路径:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["dapao", "PNG", 100, true, ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
