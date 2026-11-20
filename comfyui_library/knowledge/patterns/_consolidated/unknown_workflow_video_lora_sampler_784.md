---
name: unknown_workflow_video_lora_sampler_784
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.909
common_nodes: [ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoPhantomEmbeds, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/电商多图参考生成视频 skyreel V3_2017384271350075393.json, 视频生成/图生视频/SkyReels V3多图参考大模型：上传两张人物照生成合拍视频！_2017184716553719810.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_784

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/电商多图参考生成视频 skyreel V3_2017384271350075393.json、视频生成/图生视频/SkyReels V3多图参考大模型：上传两张人物照生成合拍视频！_2017184716553719810.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoPhantomEmbeds`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Int` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `TextInput_` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
