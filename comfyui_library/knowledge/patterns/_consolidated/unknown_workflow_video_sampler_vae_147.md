---
name: unknown_workflow_video_sampler_vae_147
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.739667
common_nodes: [CR Prompt Text, ImagePadKJ, JWInteger, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoModelLoader, WanVideoPhantomEmbeds, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1936769465738514434.json, 视频生成/图生视频/1927406902211416066.json, 视频生成/图生视频/1916898231614111746.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_147

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/1936769465738514434.json、视频生成/图生视频/1927406902211416066.json、视频生成/图生视频/1916898231614111746.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 3 个 workflow 都包含：
- `CR Prompt Text`
- `ImagePadKJ`
- `JWInteger`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoModelLoader`
- `WanVideoPhantomEmbeds`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 2/3 个有
- `ImageResizeKJ` —— 2/3 个有
- `WanVideoTorchCompileSettings` —— 2/3 个有
- `GetNode` —— 1/3 个有
- `ImageConcanate` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `LayerUtility: PurgeVRAM V2` —— 1/3 个有
- `Note Plus (mtb)` —— 1/3 个有
- `PDIMAGE_LongerSize` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `VHS_Unbatch` —— 1/3 个有
- `WanVideoEnhanceAVideo` —— 1/3 个有
- `WanVideoExperimentalArgs` —— 1/3 个有
- `WanVideoSLG` —— 1/3 个有
- `WanVideoVRAMManagement` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
