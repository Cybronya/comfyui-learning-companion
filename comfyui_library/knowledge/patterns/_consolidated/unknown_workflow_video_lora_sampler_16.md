---
name: unknown_workflow_video_lora_sampler_16
type: Unknown Workflow
frequency: 37
level: moderate
coverage: 0.525595
common_nodes: [BatchCount+, CLIPVisionLoader, DrawViTPose, ImageBatch, ImageFromBatch, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, PreviewImage, RepeatImageBatch, VHS_VideoCombine, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoLoraSelect, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, easy float, easy mathInt]
problems: []
missing: []
members: [视频生成/图生视频/【动作迁移】wan22animate_单人版_2098717884812976129.json, 视频生成/图生视频/2045891229149302786.json, 视频生成/图生视频/2032851375377354753.json, 视频生成/图生视频/2058093873213296642.json, 视频生成/图生视频/2075200788628070401.json, 视频生成/图生视频/2040058944869113857.json, 视频生成/图生视频/2031729739819393025.json, 视频生成/图生视频/超强 动作迁移 高精细动作模仿 需要plus_2084240017639170050.json, 视频生成/图生视频/2078317675809431553.json, 视频生成/图生视频/2056347634981494785.json, 视频生成/图生视频/2079900208376410113.json, 视频生成/图生视频/2079451577068384257.json, 视频生成/图生视频/2060595760235892737.json, 视频生成/图生视频/2062202323358806018.json, 视频生成/图生视频/2059569545886654466.json, 视频生成/图生视频/2059625693083951106.json, 视频生成/图生视频/2059626029299359746.json, 视频生成/图生视频/2059651380591284225.json, 视频生成/图生视频/2059655800087465986.json, 视频生成/图生视频/2059655902189412353.json, 视频生成/图生视频/2059659749129543682.json, 视频生成/图生视频/2060328341084921857.json, 视频生成/图生视频/2043400679816962049.json, 视频生成/图生视频/2052270190972420097.json, 视频生成/图生视频/2056605663723352066.json, 视频生成/图生视频/2056901108127330305.json, 视频生成/图生视频/2074305725089804289.json, 视频生成/图生视频/2078408880727609346.json, 视频生成/图生视频/2078464035640668161.json, 视频生成/图生视频/高精动作模仿 只模仿动作跳舞模仿 1：1复刻动作_2099818962723889154.json, 视频生成/图生视频/高精动作模仿 只模仿动作跳舞模仿 1：1复刻动作_2099839308415979522.json, 视频生成/图生视频/2080183256737210370.json, 视频生成/图生视频/2077952800755118081.json, 视频生成/图生视频/2078675405703307266.json, 视频生成/图生视频/高精细1_1复刻动作迁移，动作模仿plus版_2084239498350776322.json, 视频生成/图生视频/2078075351011520514.json, 视频生成/图生视频/高质量动作迁移人物精细 高级强化版_2083007472301858818.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_16

> 由 `engine/knowledge_consolidation` 从 37 个 workflow 归纳得出（视频生成/图生视频/【动作迁移】wan22animate_单人版_2098717884812976129.json、视频生成/图生视频/2045891229149302786.json、视频生成/图生视频/2032851375377354753.json、视频生成/图生视频/2058093873213296642.json、视频生成/图生视频/2075200788628070401.json…）

- **类型**：Unknown Workflow
- **样本数**：37
- **可信度**：中等可信
- **平均知识覆盖**：53%

## 共有节点

全部 37 个 workflow 都包含：
- `BatchCount+`
- `CLIPVisionLoader`
- `DrawViTPose`
- `ImageBatch`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `PreviewImage`
- `RepeatImageBatch`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `easy float`
- `easy mathInt`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 36/37 个有
- `SetNode` —— 36/37 个有
- `VRAMReserver` —— 36/37 个有
- `Int` —— 35/37 个有
- `RHHiddenNodes` —— 35/37 个有
- `VHS_LoadVideo` —— 35/37 个有
- `easy cleanGpuUsed` —— 35/37 个有
- `easy showAnything` —— 34/37 个有
- `MemoryCleaner` —— 33/37 个有
- `CR Text` —— 2/37 个有
- `VHS_LoadVideoFFmpeg` —— 2/37 个有
- `easy int` —— 2/37 个有
- `CM_FloatToInt` —— 1/37 个有
- `CompressImages` —— 1/37 个有
- `CreateVideo` —— 1/37 个有
- `ImageConcatMulti` —— 1/37 个有
- `Label (rgthree)` —— 1/37 个有
- `LayerUtility: PurgeVRAM V2` —— 1/37 个有
- `LoadVideo` —— 1/37 个有
- `SDPoseOODLoader` —— 1/37 个有
- `SDPoseOODProcessor` —— 1/37 个有
- `SaveVideo` —— 1/37 个有
- `VHS_SelectFilename` —— 1/37 个有
- `easy promptConcat` —— 1/37 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
