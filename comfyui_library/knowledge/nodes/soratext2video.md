# SoraText2Video

## 节点类型

`SoraText2Video`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `prompt:STRING`（1 次）
- `model:COMBO`（1 次）
- `duration_sora2:COMBO`（1 次）
- `duration_sora2pro:COMBO`（1 次）
- `api_base:STRING`（1 次）
- `api_key:STRING`（1 次）
- `orientation:COMBO`（1 次）
- `size:COMBO`（1 次）
- `watermark:BOOLEAN`（1 次）
- `timeout:INT`（1 次）

## 输出

- `任务ID:STRING`（1 次）
- `状态:STRING`（1 次）
- `状态更新时间:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "sora-2", "15", "15", "https://api.kegeai.top", "", "portrait", "large", false, 120]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
