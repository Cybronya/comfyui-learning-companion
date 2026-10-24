---
name: text_to_image_controlnet_sampler_clip_7
type: Text To Image
frequency: 6
level: moderate
coverage: 0.856
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, EmptyLatentImage, KSampler, LoadImage, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/【人物一致性】【洗图专用】美女换脸换衣_1908918958693429250.json, 图片生成/图生图/【角色一致性】【洗图专用】小红书抖音爆款美女_1906726533422100482.json, 图片生成/图生图/人物随意更换服装工作流_1914924421117870081.json, 图片生成/文生图/Controlnet控制_2008470287586693121.json, 图片生成/文生图/controlnet工作流_1982352014791319553.json, 图片生成/文生图/文生图基础款+ controlnet工作流_1978737989356556290.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_sampler_clip_7

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/【人物一致性】【洗图专用】美女换脸换衣_1908918958693429250.json、图片生成/图生图/【角色一致性】【洗图专用】小红书抖音爆款美女_1906726533422100482.json、图片生成/图生图/人物随意更换服装工作流_1914924421117870081.json、图片生成/文生图/Controlnet控制_2008470287586693121.json、图片生成/文生图/controlnet工作流_1982352014791319553.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 5/6 个有
- `AIO_Preprocessor` —— 4/6 个有
- `LoraLoader` —— 4/6 个有
- `Anything Everywhere` —— 3/6 个有
- `Get Image Size` —— 3/6 个有
- `RescaleCFG` —— 3/6 个有
- `CR Text` —— 2/6 个有
- `CR Text Concatenate` —— 2/6 个有
- `Image Comparer (rgthree)` —— 2/6 个有
- `workflow>姿势控制` —— 2/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 640 | 512 - 1024 | 6 | 72% |
| 高度 | 768 | 512 - 1024 | 6 | 67% |
| 采样步数 | 20 | 15 - 30 | 6 | 78% |
| Prompt 约束强度(CFG) | 3.05 | 3 - 7 | 6 | 61% |
| 采样算法 | dpmpp_sde | - | 6 | 50% |
| 调度器 | karras | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| ControlNet 权重 | 0.75 | 0.7 - 1 | 6 | 84% |
| LoRA 模型强度 | 1 | 1 - 1 | 4 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 640，观测区间 512 - 1024，6 个样本
- 高度 中位数 768，观测区间 512 - 1024，6 个样本
- 采样步数 中位数 20，观测区间 15 - 30，6 个样本
- Prompt 约束强度(CFG) 中位数 3.05，观测区间 3 - 7，6 个样本
- 采样算法 最常用 dpmpp_sde，6 个样本，一致性 50%
- 调度器 最常用 karras，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.75，观测区间 0.7 - 1，6 个样本，取值集中（一致性 84%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
