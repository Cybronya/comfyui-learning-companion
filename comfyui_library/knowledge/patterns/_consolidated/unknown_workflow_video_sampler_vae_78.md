---
name: unknown_workflow_video_sampler_vae_78
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.905833
common_nodes: [VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/【遇见AI】wan2.1 phantom多角色一致性_2066436467760652289.json, 图片生成/文生图/【遇见AI】wan2.1文生视频基础流，带加速_2061013216846770177.json, 视频生成/图生视频/phantom视频界的万物迁移_1942392915929010177.json, 视频生成/图生视频/phontom 多图参考_1928118108420980738.json, 视频生成/图生视频/【遇见AI】wan2.1 skyreels V3 R2V多图参考模型_2067524642499289090.json, 视频生成/图生视频/多参考一致性视频_Phantom_1927430164823564289.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_78

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/【遇见AI】wan2.1 phantom多角色一致性_2066436467760652289.json、图片生成/文生图/【遇见AI】wan2.1文生视频基础流，带加速_2061013216846770177.json、视频生成/图生视频/phantom视频界的万物迁移_1942392915929010177.json、视频生成/图生视频/phontom 多图参考_1928118108420980738.json、视频生成/图生视频/【遇见AI】wan2.1 skyreels V3 R2V多图参考模型_2067524642499289090.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 6 个 workflow 都包含：
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 5/6 个有
- `WanVideoEncode` —— 5/6 个有
- `WanVideoLoraSelect` —— 5/6 个有
- `WanVideoPhantomEmbeds` —— 5/6 个有
- `WanVideoTorchCompileSettings` —— 5/6 个有
- `ImageResizeKJ` —— 4/6 个有
- `PreviewImage` —— 4/6 个有
- `LoadWanVideoT5TextEncoder` —— 3/6 个有
- `WanVideoSetBlockSwap` —— 3/6 个有
- `WanVideoSetLoRAs` —— 3/6 个有
- `WanVideoTextEncode` —— 3/6 个有
- `WanVideoTextEncodeCached` —— 3/6 个有
- `DownloadAndLoadGIMMVFIModel` —— 2/6 个有
- `GIMMVFI_interpolate` —— 2/6 个有
- `INTConstant` —— 2/6 个有
- `easy imageRemBg` —— 2/6 个有
- `ImagePadKJ` —— 1/6 个有
- `ImageResizeKJv2` —— 1/6 个有
- `Int` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有
- `LayerUtility: PurgeVRAM V2` —— 1/6 个有
- `WanVideoEmptyEmbeds` —— 1/6 个有
- `WanVideoVRAMManagement` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
