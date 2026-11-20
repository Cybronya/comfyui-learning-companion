---
name: unknown_workflow_video_sampler_clip_61
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8678
common_nodes: [LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageClipEncode, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/CFG Zreo Star万相图生视频_1907807736166232066.json, 视频生成/图生视频/SkyReels  图生视频加速版_1932067236700127234.json, 视频生成/图生视频/SkyReels V2 161帧长序列稳定性图生视频优化版V1_1914225072540741633.json, 视频生成/图生视频/SkyReels V2 161帧长序列稳定性图生视频优化版_1914706731866255362.json, 视频生成/图生视频/SkyReels V2 图生视频_1926816500064358401.json, 视频生成/图生视频/WAN复杂动作防崩图生视频工作流V5（调整模型缩放）_1905280453560176642.json, 视频生成/图生视频/Wan kijai版-SLG模式_1903813340349501441.json, 视频生成/图生视频/Wan图生视频Latent保存本地解码工作流_1913242706372456449.json, 视频生成/图生视频/（自用）Wan图生视频Latent保存工作流_1911248941428736001.json, 视频生成/图生视频/🦖SkyReels V2 161帧图生视频_1914494071358877697.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_61

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/CFG Zreo Star万相图生视频_1907807736166232066.json、视频生成/图生视频/SkyReels  图生视频加速版_1932067236700127234.json、视频生成/图生视频/SkyReels V2 161帧长序列稳定性图生视频优化版V1_1914225072540741633.json、视频生成/图生视频/SkyReels V2 161帧长序列稳定性图生视频优化版_1914706731866255362.json、视频生成/图生视频/SkyReels V2 图生视频_1926816500064358401.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 10 个 workflow 都包含：
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageClipEncode`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoExperimentalArgs` —— 9/10 个有
- `JWInteger` —— 8/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/10 个有
- `LayerUtility: PurgeVRAM` —— 8/10 个有
- `WanVideoEnhanceAVideo` —— 8/10 个有
- `CR Prompt Text` —— 7/10 个有
- `Note Plus (mtb)` —— 3/10 个有
- `HyVideoEnhanceAVideo` —— 2/10 个有
- `LTXVPromptEnhancer` —— 2/10 个有
- `LTXVPromptEnhancerLoader` —— 2/10 个有
- `LoadLatent` —— 2/10 个有
- `SaveImage` —— 2/10 个有
- `SaveLatent` —— 2/10 个有
- `PrimitiveInt` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
