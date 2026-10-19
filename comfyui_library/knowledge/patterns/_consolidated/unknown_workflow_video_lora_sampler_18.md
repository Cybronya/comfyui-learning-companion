---
name: unknown_workflow_video_lora_sampler_18
type: Unknown Workflow
frequency: 32
level: moderate
coverage: 0.687625
common_nodes: [BasicScheduler, BatchImagesNode, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, ColorTransfer, DiffusionModelLoaderKJ, GetImageRangeFromBatch, ImageResizeKJv2, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PreviewAny, PreviewImage, SAM3_VideoTrack, SCAIL2ColoredMask, SamplerCustom, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanSCAILToVideo]
problems: []
missing: []
members: [视频生成/图生视频/2075508947406114818.json, 视频生成/图生视频/SCAIL2 动作迁移+角色替换_2085192450951438337.json, 视频生成/图生视频/SCAIL2 动作迁移+角色替换_2085200053362323457.json, 视频生成/图生视频/SCAIL2 动作迁移+角色替换_2085526911635247106.json, 视频生成/图生视频/SCAIL2-动作迁移 不限时长  复刻跳舞动作 单人跳舞 复刻动作_2083867987425193985.json, 视频生成/图生视频/SCAIL2-动作迁移 不限时长  复刻跳舞动作 单人跳舞 复刻动作_2087530408845074433.json, 视频生成/图生视频/SCAIL2-动作迁移 不限时长  复刻跳舞动作 单人跳舞 复刻动作_2089613034095468546.json, 视频生成/图生视频/2073276130169278465.json, 视频生成/图生视频/2073308786999259137.json, 视频生成/图生视频/2077003812061147137.json, 视频生成/图生视频/SCAIL2-动作迁移 不限时长  复刻跳舞动作 单人跳舞_2089596899274874881.json, 视频生成/图生视频/SCAIL2-动作迁移 不限时长  复刻跳舞动作 单人跳舞_2103438449415114754.json, 视频生成/图生视频/SCAIL2-动作迁移 不限时长  复刻跳舞动作 单人跳舞_2103447110430576641.json, 视频生成/图生视频/SCAIL2-动作迁移 不限时长_2100214925217062914.json, 视频生成/图生视频/SCAIL2-动作迁移 不限时长_2108431179807551490.json, 视频生成/图生视频/Scail2-动作迁移（单人+多人版）_2065351817646661633.json, 视频生成/图生视频/2065037170393575426.json, 视频生成/图生视频/2066326016666202113.json, 视频生成/图生视频/2070098008229896194.json, 视频生成/图生视频/2072654435834228737.json, 视频生成/图生视频/2080322084730916866.json, 视频生成/图生视频/2080326375218704385.json, 视频生成/图生视频/2065001681598902273.json, 视频生成/图生视频/2064895115918929922.json, 视频生成/图生视频/2068508853481861121.json, 视频生成/图生视频/pipi-SCAIL2-动作迁移 不限时长 （国内版）_2068457565150867458.json, 视频生成/图生视频/2072184154577530881.json, 视频生成/图生视频/2065350812397817858.json, 视频生成/图生视频/2065428476076843010.json, 视频生成/图生视频/2065454404580495362.json, 视频生成/图生视频/2065428027999342594.json, 视频生成/图生视频/2069813471377711106.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_18

> 由 `engine/knowledge_consolidation` 从 32 个 workflow 归纳得出（视频生成/图生视频/2075508947406114818.json、视频生成/图生视频/SCAIL2 动作迁移+角色替换_2085192450951438337.json、视频生成/图生视频/SCAIL2 动作迁移+角色替换_2085200053362323457.json、视频生成/图生视频/SCAIL2 动作迁移+角色替换_2085526911635247106.json、视频生成/图生视频/SCAIL2-动作迁移 不限时长  复刻跳舞动作 单人跳舞 复刻动作_2083867987425193985.json…）

- **类型**：Unknown Workflow
- **样本数**：32
- **可信度**：中等可信
- **平均知识覆盖**：69%

## 共有节点

全部 32 个 workflow 都包含：
- `BasicScheduler`
- `BatchImagesNode`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ColorTransfer`
- `DiffusionModelLoaderKJ`
- `GetImageRangeFromBatch`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PreviewAny`
- `PreviewImage`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `SamplerCustom`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanSCAILToVideo`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 28/32 个有
- `GetImageSize` —— 28/32 个有
- `JWInteger` —— 28/32 个有
- `TensorLoopClose` —— 28/32 个有
- `TensorLoopOpen` —— 28/32 个有
- `PrimitiveInt` —— 27/32 个有
- `CR Prompt Text` —— 17/32 个有
- `Seed (rgthree)` —— 17/32 个有
- `ShowAnything|Mie` —— 17/32 个有
- `VHS_VideoInfo` —— 17/32 个有
- `WanChunkFeedForward` —— 17/32 个有
- `DownloadAndLoadGIMMVFIModel` —— 15/32 个有
- `GIMMVFI_interpolate` —— 15/32 个有
- `SetNode` —— 15/32 个有
- `EmptyImage` —— 14/32 个有
- `GetNode` —— 14/32 个有
- `ImageCompositeMasked` —— 14/32 个有
- `ImageConcatMulti` —— 14/32 个有
- `ResizeImageMaskNode` —— 14/32 个有
- `SAM3_TrackToMask` —— 14/32 个有
- `easy showAnything` —— 6/32 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/32 个有
- `SizeSelector` —— 5/32 个有
- `VHS_VideoInfoSource` —— 5/32 个有
- `easy imageCount` —— 5/32 个有
- `Bjornulf_ShowInt` —— 4/32 个有
- `Int` —— 3/32 个有
- `ComfySwitchNode` —— 1/32 个有
- `ImageCrop` —— 1/32 个有
- `ImagePadKJ` —— 1/32 个有
- `MathExpression|pysssss` —— 1/32 个有
- `PrimitiveBoolean` —— 1/32 个有
- `RH_Captioner` —— 1/32 个有
- `ReActorFaceSwap` —— 1/32 个有
- `RemoveWatermarks_LoadModel` —— 1/32 个有
- `RemoveWatermarks_Run` —— 1/32 个有
- `RunningHub Deepcleaner` —— 1/32 个有
- `Text` —— 1/32 个有
- `ToFloat` —— 1/32 个有
- `easy cleanGpuUsed` —— 1/32 个有
- `easy indexAnything` —— 1/32 个有
- `string_util_StrConcat` —— 1/32 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
