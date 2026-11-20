---
name: unknown_workflow_video_lora_sampler_976
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.981
common_nodes: [BerniniBlockSwap, BerniniLoraSelectMulti, CLIPVisionLoader, CR Prompt Text, ComfyNumberConvert, ImageResizeKJv2, Int, LoadImage, MathExpression|pysssss, VHS_LoadVideo, VHS_VideoCombine, WanAnimatePlus ClipVisionEncode, WanAnimatePlus Decode, WanAnimatePlus ModelLoader, WanAnimatePlus SCAIL_2 Embeds, WanAnimatePlus Sampler, WanAnimatePlus TextEncodeCached, WanAnimatePlus VAELoader]
problems: []
missing: []
members: [平台全量/Scail2-动作迁移+参考背景_2066129221889650689.json, 平台全量/Scail2-视频背景指定图像更换_2066147450641010690.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_976

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/Scail2-动作迁移+参考背景_2066129221889650689.json、平台全量/Scail2-视频背景指定图像更换_2066147450641010690.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：98%

## 共有节点

全部 2 个 workflow 都包含：
- `BerniniBlockSwap`
- `BerniniLoraSelectMulti`
- `CLIPVisionLoader`
- `CR Prompt Text`
- `ComfyNumberConvert`
- `ImageResizeKJv2`
- `Int`
- `LoadImage`
- `MathExpression|pysssss`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanAnimatePlus ClipVisionEncode`
- `WanAnimatePlus Decode`
- `WanAnimatePlus ModelLoader`
- `WanAnimatePlus SCAIL_2 Embeds`
- `WanAnimatePlus Sampler`
- `WanAnimatePlus TextEncodeCached`
- `WanAnimatePlus VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageFromBatch` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `easy imageRemBg` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
