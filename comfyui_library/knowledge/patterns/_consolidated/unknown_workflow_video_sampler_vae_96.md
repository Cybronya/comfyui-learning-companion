---
name: unknown_workflow_video_sampler_vae_96
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9834
common_nodes: [JWInteger, LayerUtility: PurgeVRAM V2, LoadWanVideoT5TextEncoder, Text, VHS_VideoCombine, VideoCombine_Adv, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoMagCache, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncodeSingle, WanVideoVACEEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1937000254204186626.json, 视频生成/图生视频/1936801128262832130.json, 视频生成/图生视频/1934980178835906562.json, 视频生成/图生视频/1935329421408796673.json, 视频生成/文生视频/1935708946168803329.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_96

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/1937000254204186626.json、视频生成/图生视频/1936801128262832130.json、视频生成/图生视频/1934980178835906562.json、视频生成/图生视频/1935329421408796673.json、视频生成/文生视频/1935708946168803329.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 5 个 workflow 都包含：
- `JWInteger`
- `LayerUtility: PurgeVRAM V2`
- `LoadWanVideoT5TextEncoder`
- `Text`
- `VHS_VideoCombine`
- `VideoCombine_Adv`
- `WanVideoApplyNAG`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoMagCache`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncodeSingle`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize+` —— 4/5 个有
- `ImageScale` —— 4/5 个有
- `LoadImage` —— 4/5 个有
- `WanVideoVACEStartToEndFrame` —— 2/5 个有
- `PreviewImage` —— 1/5 个有
- `Primitive integer [Crystools]` —— 1/5 个有
- `RH_ComfyFluxKontext` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
