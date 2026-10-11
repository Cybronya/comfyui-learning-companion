# DapaoGrokVideoNode

## 节点类型

`DapaoGrokVideoNode`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `🖼️ 参考图1:IMAGE`（1 次）
- `🖼️ 参考图2:IMAGE`（1 次）
- `🖼️ 参考图3:IMAGE`（1 次）
- `🖼️ 参考图4:IMAGE`（1 次）
- `🖼️ 参考图5:IMAGE`（1 次）
- `🖼️ 参考图6:IMAGE`（1 次）
- `🖼️ 参考图7:IMAGE`（1 次）
- `📝 提示词:STRING`（1 次）
- `🤖 模型:COMBO`（1 次）
- `📐 视频比例:COMBO`（1 次）

## 输出

- `🎬 视频:VIDEO`（1 次）
- `📋 任务ID:STRING`（1 次）
- `📄 响应信息:STRING`（1 次）
- `🔗 视频URL:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["一个女人在月球跳舞", "grok-video-3", "16:9", "15", "1080P", "zhenzhen", "", 0, ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
