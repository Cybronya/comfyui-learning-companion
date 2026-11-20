---
name: unknown_workflow_video_sampler_vae_85
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.931857
common_nodes: [INTConstant, LoadImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoModelLoader, WanVideoPhantomEmbeds, WanVideoSampler, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Skyreelsv3-人物与物品一致视频生成_2020431913210617857.json, 视频生成/图生视频/Skyreelsv3-人物与物品一致视频生成tvc广告短视频_2029224724693262338.json, 视频生成/图生视频/phantom多图参考视频生成_1916457677722161154.json, 视频生成/图生视频/phontom 多图参考_1928118108420980738.json, 视频生成/图生视频/多参图片生视频skyreelsV3_2019240301956702210.json, 视频生成/图生视频/多参考一致性视频_Phantom_1927430164823564289.json, 视频生成/图生视频/稳定的图像编辑 fusionx_1934649298468708353.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_85

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/Skyreelsv3-人物与物品一致视频生成_2020431913210617857.json、视频生成/图生视频/Skyreelsv3-人物与物品一致视频生成tvc广告短视频_2029224724693262338.json、视频生成/图生视频/phantom多图参考视频生成_1916457677722161154.json、视频生成/图生视频/phontom 多图参考_1928118108420980738.json、视频生成/图生视频/多参图片生视频skyreelsV3_2019240301956702210.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 7 个 workflow 都包含：
- `INTConstant`
- `LoadImage`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoModelLoader`
- `WanVideoPhantomEmbeds`
- `WanVideoSampler`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImagePadKJ` —— 6/7 个有
- `ImageResizeKJ` —— 6/7 个有
- `LoadWanVideoT5TextEncoder` —— 5/7 个有
- `WanVideoTextEncode` —— 5/7 个有
- `PreviewImage` —— 3/7 个有
- `WanVideoEnhanceAVideo` —— 3/7 个有
- `WanVideoExperimentalArgs` —— 3/7 个有
- `WanVideoLoraSelect` —— 3/7 个有
- `WanVideoSLG` —— 3/7 个有
- `WanVideoTeaCache` —— 3/7 个有
- `WanVideoTorchCompileSettings` —— 3/7 个有
- `easy imageRemBg` —— 3/7 个有
- `SimpleMath+` —— 2/7 个有
- `WanVideoTextEncodeCached` —— 2/7 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/7 个有
- `GIMMVFI_interpolate` —— 1/7 个有
- `ImageResizeKJv2` —— 1/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有
- `LayerUtility: PurgeVRAM V2` —— 1/7 个有
- `WanVideoMagCache` —— 1/7 个有
- `WanVideoVRAMManagement` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
