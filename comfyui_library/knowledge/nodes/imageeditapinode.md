# ImageEditAPINode

## 节点类型

`ImageEditAPINode`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `🖼️ 图像1:IMAGE`（8 次）
- `🖼️ 图像2:IMAGE`（8 次）
- `🖼️ 图像3:IMAGE`（8 次）
- `🖼️ 图像4:IMAGE`（8 次）
- `💬 提示词:STRING`（8 次）
- `🌐 API地址:STRING`（8 次）
- `🔑 API密钥:STRING`（8 次）
- `🤖 模型名称:STRING`（8 次）
- `📡 请求方法:COMBO`（8 次）
- `🔐 密钥位置:COMBO`（8 次）

## 输出

- `image:IMAGE`（8 次）
- `response:STRING`（8 次）
- `image_url:STRING`（8 次）
- `raw_json:STRING`（8 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["请根据这些图片进行专业的图像编辑", "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-image-preview:generateContent`（2 次）
- `["请根据这些图片进行专业的图像编辑", "https://api.gptbest.vip/v1/chat/completions", "", "gemini-3-pro-image-preview", "POST", "Header", `（2 次）
- `["请根据这些图片进行专业的图像编辑", "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-image-preview:generateContent`（1 次）
- `["请根据这些图片进行专业的图像编辑", "https://api.gptbest.vip/v1/chat/completions", "", "nano-banana-2-4k", "POST", "Header", "Authoriza`（1 次）
- `["爆发力十足的年轻女歌手，面部表情激动，眼神充满力量与投入，真实的皮肤纹理.发丝细节.汗水浸透的发梢，紧握复古麦克风仰天嘶吼，另一只手高举过头顶，身体大幅度后倾，汗珠飞溅，脖颈青筋暴起，闪亮钉珠的黑色紧身皮质连体衣+高筒铆钉皮靴，臂钏和锁`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
