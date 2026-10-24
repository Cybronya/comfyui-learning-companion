---
name: unknown_workflow_video_sampler_unet_63
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.79275
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/h3-角色人物场景生成视频_2094058724343246849.json, 视频生成/图生视频/电商产品展示 图片参考生视频 minimax h3_2085356615661875201.json, 视频生成/文生视频/MinimaxH3多人物短剧工作流竖屏(提示词优化+量化加速版)_2084915488760619009.json, 视频生成/文生视频/Minimax多人物多参短剧工作流(量化加速版)_2084650866472214530.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_63

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/h3-角色人物场景生成视频_2094058724343246849.json、视频生成/图生视频/电商产品展示 图片参考生视频 minimax h3_2085356615661875201.json、视频生成/文生视频/MinimaxH3多人物短剧工作流竖屏(提示词优化+量化加速版)_2084915488760619009.json、视频生成/文生视频/Minimax多人物多参短剧工作流(量化加速版)_2084650866472214530.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 4 个 workflow 都包含：
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
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 3/4 个有
- `EasyCache` —— 3/4 个有
- `GetVideoComponents` —— 3/4 个有
- `PathchSageAttentionKJ` —— 3/4 个有
- `PrimitiveStringMultiline` —— 3/4 个有
- `JjkText` —— 2/4 个有
- `PreviewAny` —— 2/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `FlashVSRNode` —— 1/4 个有
- `GetImagesFromBatchIndexed` —— 1/4 个有
- `ModelAttentionBackend` —— 1/4 个有
- `RH_LLMAPI_Pro_Node` —— 1/4 个有
- `SaveImage` —— 1/4 个有
- `Sleep` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
