---
name: unknown_workflow_video_sampler_vae_177
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8905
common_nodes: [JWInteger, LoadWanVideoT5TextEncoder, Primitive integer [Crystools], VHS_VideoCombine, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoMagCache, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncodeSingle, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/文生图/最强文生视频FusionX最强文生视频+自动扩写提示词+补针流畅运行万相wan2.1_1933801723888586754.json, 视频生成/文生视频/FusionX Nag版双重加速文生视频V1（支持负面词禁用）_1933931993669525506.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_177

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/最强文生视频FusionX最强文生视频+自动扩写提示词+补针流畅运行万相wan2.1_1933801723888586754.json、视频生成/文生视频/FusionX Nag版双重加速文生视频V1（支持负面词禁用）_1933931993669525506.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `JWInteger`
- `LoadWanVideoT5TextEncoder`
- `Primitive integer [Crystools]`
- `VHS_VideoCombine`
- `WanVideoApplyNAG`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoMagCache`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncodeSingle`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/2 个有
- `Float` —— 1/2 个有
- `GIMMVFI_interpolate` —— 1/2 个有
- `LayerUtility: PurgeVRAM` —— 1/2 个有
- `LayerUtility: PurgeVRAM V2` —— 1/2 个有
- `RH_OneShot_Prompter` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
