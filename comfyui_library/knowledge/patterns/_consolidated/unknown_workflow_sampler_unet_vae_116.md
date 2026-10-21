---
name: unknown_workflow_sampler_unet_vae_116
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.780857
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Minimax h3 故事多分镜图处理_2096523123339386881.json, 视频生成/图生视频/Minimax h3 高一致性-故事多分镜图处理_2103117440178810882.json, 视频生成/图生视频/Minimax+H3+多图生视频声音一致性工作流_2084677543038377986.json, 视频生成/图生视频/Minimax-H3-R2V 开源版本 多参考生视频_2084285644305682434.json, 视频生成/图生视频/Minimax-H3-图生视频（Lightx2v正式版）_2087553566264356865.json, 视频生成/图生视频/Minimax-H3-多参-长视频-原版-736p直出_2096509767048060930.json, 视频生成/图生视频/h3-角色人物场景生成视频_2094058724343246849.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_116

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/Minimax h3 故事多分镜图处理_2096523123339386881.json、视频生成/图生视频/Minimax h3 高一致性-故事多分镜图处理_2103117440178810882.json、视频生成/图生视频/Minimax+H3+多图生视频声音一致性工作流_2084677543038377986.json、视频生成/图生视频/Minimax-H3-R2V 开源版本 多参考生视频_2084285644305682434.json、视频生成/图生视频/Minimax-H3-图生视频（Lightx2v正式版）_2087553566264356865.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 6/7 个有
- `PrimitiveStringMultiline` —— 6/7 个有
- `ModelAttentionBackend` —— 5/7 个有
- `Fast Groups Bypasser (rgthree)` —— 4/7 个有
- `VHS_VideoCombine` —— 4/7 个有
- `GetImagesFromBatchIndexed` —— 3/7 个有
- `GetVideoComponents` —— 3/7 个有
- `SaveImage` —— 3/7 个有
- `SaveVideo` —— 3/7 个有
- `LoadAudio` —— 2/7 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/7 个有
- `FlashVSRNode` —— 1/7 个有
- `JjkText` —— 1/7 个有
- `LoadVideoUI` —— 1/7 个有
- `LoraLoaderModelOnly` —— 1/7 个有
- `MiniMaxH3MotionContext` —— 1/7 个有
- `MiniMaxH3MotionContextTrim` —— 1/7 个有
- `MiniMaxH3SigmaShift` —— 1/7 个有
- `PreviewAny` —— 1/7 个有
- `RH_LLMAPI_Pro_Node` —— 1/7 个有
- `Sleep` —— 1/7 个有
- `孤海注释` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
