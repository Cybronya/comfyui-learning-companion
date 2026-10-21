# DapaoDetailFlowPromptNode

## 节点类型

`DapaoDetailFlowPromptNode`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `🔗 外部原始需求:STRING`（1 次）
- `📦 产品图1:IMAGE`（1 次）
- `📦 产品图2:IMAGE`（1 次）
- `📦 产品图3:IMAGE`（1 次）
- `📦 产品图4:IMAGE`（1 次）
- `📦 产品图5:IMAGE`（1 次）
- `📦 产品图6:IMAGE`（1 次）
- `🎨 风格参考图1:IMAGE`（1 次）
- `🎨 风格参考图2:IMAGE`（1 次）
- `🎨 风格参考图3:IMAGE`（1 次）

## 输出

- `🧭 可选视觉母版提示词:STRING`（1 次）
- `🖼️ 第01屏提示词:STRING`（1 次）
- `🖼️ 第02屏提示词:STRING`（1 次）
- `🖼️ 第03屏提示词:STRING`（1 次）
- `🖼️ 第04屏提示词:STRING`（1 次）
- `🖼️ 第05屏提示词:STRING`（1 次）
- `🖼️ 第06屏提示词:STRING`（1 次）
- `🖼️ 第07屏提示词:STRING`（1 次）
- `🖼️ 第08屏提示词:STRING`（1 次）
- `📋 详情页完整蓝图JSON:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "gemini-3.7-flash", "实体商品详情页", "自动识别", "淘宝/天猫", "8", "严格连续详情页（推荐）", "自动规划不同屏文字（推荐）", "自动生成可选母版提示词（推荐）", "GPT Image `（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
