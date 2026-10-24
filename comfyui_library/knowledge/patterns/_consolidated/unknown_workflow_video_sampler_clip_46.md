---
name: unknown_workflow_video_sampler_clip_46
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.887182
common_nodes: [LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageClipEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/父子打架_1963882949047455746.json, 视频生成/图生视频/11111lora_1943131304420663297.json, 视频生成/图生视频/360度无限旋转-万相wan2.1新玩法_1925020380900356097.json, 视频生成/图生视频/wan2.1-i2v-360度旋转_1899839551614115842.json, 视频生成/图生视频/wan2.1-i2v-图生视频_1862829335932547073.json, 视频生成/图生视频/wan2.1-i2v-飞天特效_1899833123503222786.json, 视频生成/图生视频/wan2.1_1936400345864245250.json, 视频生成/图生视频/万能通用测试万相lora_1942427410207813634.json, 视频生成/图生视频/拉近眼睛镜头万相图生视48工作流_1938430134720593922.json, 视频生成/图生视频/缩小到地球万相图生视50工作流_1938457014647324673.json, 视频生成/图生视频/跳踢倒50_1940619360874508289.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_46

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/父子打架_1963882949047455746.json、视频生成/图生视频/11111lora_1943131304420663297.json、视频生成/图生视频/360度无限旋转-万相wan2.1新玩法_1925020380900356097.json、视频生成/图生视频/wan2.1-i2v-360度旋转_1899839551614115842.json、视频生成/图生视频/wan2.1-i2v-图生视频_1862829335932547073.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 11 个 workflow 都包含：
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageClipEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoLoraSelect` —— 10/11 个有
- `DownloadAndLoadGIMMVFIModel` —— 8/11 个有
- `GIMMVFI_interpolate` —— 8/11 个有
- `LayerUtility: PurgeVRAM` —— 8/11 个有
- `WanVideoTorchCompileSettings` —— 7/11 个有
- `UpscaleModelLoader` —— 6/11 个有
- `WanVideoExperimentalArgs` —— 6/11 个有
- `Fast Groups Bypasser (rgthree)` —— 4/11 个有
- `ImageScaleToMegapixels` —— 4/11 个有
- `ImageSmartSharpen+` —— 4/11 个有
- `ImageUpscaleWithModel` —— 4/11 个有
- `easy cleanGpuUsed` —— 4/11 个有
- `Int` —— 3/11 个有
- `GetNode` —— 2/11 个有
- `ImageResizeKJ` —— 2/11 个有
- `MathExpression|pysssss` —— 2/11 个有
- `SetNode` —— 2/11 个有
- `Upscale Model Loader` —— 2/11 个有
- `easy showAnything` —— 2/11 个有
- `KEEP_ModelLoader` —— 1/11 个有
- `KEEP_ProcessImageSequence` —— 1/11 个有
- `PrimitiveBoolean` —— 1/11 个有
- `VHS_LoadVideo` —— 1/11 个有
- `VHS_VideoInfo` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
