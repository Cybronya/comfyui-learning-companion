---
name: unknown_workflow_sampler_unet_vae_151
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.829143
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ImageFromBatch, ImageStitch, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveImage, StringConcatenate, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/MinimaxH3 角色六视图（自动版）_2090089945036845057.json, 图片生成/图生图/MinimaxH3 角色四视图（自动版）_2090070169673621506.json, 图片生成/图生图/Minimax_H3_生成场景_8_视图可以场景中某物为中心_2096867791893778433.json, 图片生成/图生图/Minimax_H3_生成场景_8_视图可以场景中某物为中心_2097159652462125058.json, 视频生成/图生视频/Minimax H3 生成场景 8 视图（可以场景中某物为中心）_2092374389412155393.json, 视频生成/图生视频/Minimax H3 生成角色 6 视图 + 360°旋转+人脸特写 视频_2092354483618672642.json, 视频生成/图生视频/【老金驿站】MinimaxH3生成人物三视图工作流_2089550852343291906.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_151

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/MinimaxH3 角色六视图（自动版）_2090089945036845057.json、图片生成/图生图/MinimaxH3 角色四视图（自动版）_2090070169673621506.json、图片生成/图生图/Minimax_H3_生成场景_8_视图可以场景中某物为中心_2096867791893778433.json、图片生成/图生图/Minimax_H3_生成场景_8_视图可以场景中某物为中心_2097159652462125058.json、视频生成/图生视频/Minimax H3 生成场景 8 视图（可以场景中某物为中心）_2092374389412155393.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ImageFromBatch`
- `ImageStitch`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `StringConcatenate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MiniMaxChunkFeedForward` —— 4/7 个有
- `ModelAttentionBackend` —— 4/7 个有
- `ModelPatchTorchSettings` —— 4/7 个有
- `ResolutionSelector` —— 4/7 个有
- `BatchImagesNode` —— 3/7 个有
- `MiniMaxH3SigmaShift` —— 3/7 个有
- `CR Text` —— 2/7 个有
- `CreateVideo` —— 2/7 个有
- `LTX_lora_loader` —— 2/7 个有
- `LoraLoaderModelOnly` —— 2/7 个有
- `PreviewAny` —— 2/7 个有
- `RHLLMChatNode` —— 2/7 个有
- `SaveVideo` —— 2/7 个有
- `AILab_QwenVL` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
