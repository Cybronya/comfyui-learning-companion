---
name: unknown_workflow_video_sampler_vae_22
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.841
common_nodes: [LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEnhanceAVideo, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/wan2.1图生视频_1953157903052115969.json, 视频生成/图生视频/加速版AccVideo-T2V文生视频_1927653571515564034.json, 视频生成/文生视频/ACCVID T2V_1927061594801602561.json, 视频生成/文生视频/AniWan+Lightx2v Rank128版文生视频动漫视频_1945514035464871938.json, 视频生成/文生视频/AniWan-T2V高质量动漫视频_1945161336017887233.json, 视频生成/文生视频/AniWan-T2V高质量动漫视频llightx2v对比_1945282469895577601.json, 视频生成/文生视频/AniWan高质量动漫特化文生视频加速版V1_1944784039897124865.json, 视频生成/文生视频/EASY CACHE+LightX2v Rank64超高质量+AniWan动态文生视频加速版_1945680474150772737.json, 视频生成/文生视频/FusionX最强文生视频双倍加速版高清工作流V2（修复报错）_1933552405931806721.json, 视频生成/文生视频/LightX2v + AniWan2.1 加速文生视频｜动漫_1946107051233734657.json, 视频生成/文生视频/LightX2v Rank64极限质量+AniWan超高动态文生视频加速版V1_1945362507747794946.json, 视频生成/文生视频/LightX2v Rank64极限质量+AniWan超高动态文生视频加速版V1_2028374929778937857.json, 视频生成/文生视频/LightX2v+Rank64极限质量+AniWan超高动态文生视频加速版V1_2035902373071163394.json, 视频生成/文生视频/Pusa+Lightx2v文生视频_1945801674319601665.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_22

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/wan2.1图生视频_1953157903052115969.json、视频生成/图生视频/加速版AccVideo-T2V文生视频_1927653571515564034.json、视频生成/文生视频/ACCVID T2V_1927061594801602561.json、视频生成/文生视频/AniWan+Lightx2v Rank128版文生视频动漫视频_1945514035464871938.json、视频生成/文生视频/AniWan-T2V高质量动漫视频_1945161336017887233.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 14 个 workflow 都包含：
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
- `Primitive integer [Crystools]` —— 12/14 个有
- `WanVideoExperimentalArgs` —— 12/14 个有
- `Text Multiline` —— 11/14 个有
- `WanVideoLoraSelect` —— 10/14 个有
- `WanVideoSLG` —— 9/14 个有
- `WanVideoTeaCache` —— 9/14 个有
- `JWInteger` —— 7/14 个有
- `WanVideoTorchCompileSettings` —— 6/14 个有
- `WanVideoFreeInitArgs` —— 4/14 个有
- `Fast Groups Bypasser (rgthree)` —— 3/14 个有
- `ShowText` —— 3/14 个有
- `LoadAndResizeImage` —— 1/14 个有
- `RH_LLMAPI_NODE` —— 1/14 个有
- `RH_Translator` —— 1/14 个有
- `Text Concatenate` —— 1/14 个有
- `WanVideoEasyCache` —— 1/14 个有
- `WanVideoImageToVideoEncode` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
