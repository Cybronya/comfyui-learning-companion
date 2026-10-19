---
name: unknown_workflow_video_sampler_vae_24
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.842
common_nodes: [LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEnhanceAVideo, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1953157903052115969.json, 视频生成/图生视频/1927653571515564034.json, 视频生成/文生视频/1927061594801602561.json, 视频生成/文生视频/1945514035464871938.json, 视频生成/文生视频/1945161336017887233.json, 视频生成/文生视频/1945282469895577601.json, 视频生成/文生视频/1944784039897124865.json, 视频生成/文生视频/1945680474150772737.json, 视频生成/文生视频/1933552405931806721.json, 视频生成/文生视频/1946107051233734657.json, 视频生成/文生视频/1945362507747794946.json, 视频生成/文生视频/LightX2v Rank64极限质量+AniWan超高动态文生视频加速版V1_2028374929778937857.json, 视频生成/文生视频/LightX2v+Rank64极限质量+AniWan超高动态文生视频加速版V1_2035902373071163394.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_24

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/1953157903052115969.json、视频生成/图生视频/1927653571515564034.json、视频生成/文生视频/1927061594801602561.json、视频生成/文生视频/1945514035464871938.json、视频生成/文生视频/1945161336017887233.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 13 个 workflow 都包含：
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEnhanceAVideo`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Primitive integer [Crystools]` —— 11/13 个有
- `WanVideoExperimentalArgs` —— 11/13 个有
- `Text Multiline` —— 10/13 个有
- `WanVideoLoraSelect` —— 9/13 个有
- `WanVideoSLG` —— 9/13 个有
- `WanVideoTeaCache` —— 9/13 个有
- `JWInteger` —— 7/13 个有
- `WanVideoTorchCompileSettings` —— 5/13 个有
- `WanVideoFreeInitArgs` —— 3/13 个有
- `Fast Groups Bypasser (rgthree)` —— 2/13 个有
- `ShowText` —— 2/13 个有
- `LoadAndResizeImage` —— 1/13 个有
- `RH_Translator` —— 1/13 个有
- `WanVideoEasyCache` —— 1/13 个有
- `WanVideoImageToVideoEncode` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
