---
name: unknown_workflow_video_lora_sampler_131
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.544714
common_nodes: [BatchCount+, CLIPVisionLoader, DrawViTPose, ImageBatch, ImageFromBatch, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, PreviewImage, RepeatImageBatch, VHS_VideoCombine, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoLoraSelect, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, easy float, easy mathInt]
problems: []
missing: []
members: [视频生成/图生视频/【动作迁移】wan22animate_单人版_2098717884812976129.json, 视频生成/图生视频/动作迁移_2045891229149302786.json, 视频生成/图生视频/跑高精细的用这个动作迁移，动作高仿，需要高显存跑_2056901108127330305.json, 视频生成/图生视频/跑高精细的用这个动作迁移，还是这个版本动作模仿的好_2074305725089804289.json, 视频生成/图生视频/高精动作模仿 只模仿动作跳舞模仿 1：1复刻动作_2078408880727609346.json, 视频生成/图生视频/高精动作模仿 只模仿动作跳舞模仿 1：1复刻动作_2078464035640668161.json, 视频生成/图生视频/高精动作模仿 只模仿动作跳舞模仿 1：1复刻动作_2099818962723889154.json, 视频生成/图生视频/高精动作模仿 只模仿动作跳舞模仿 1：1复刻动作_2099839308415979522.json, 视频生成/图生视频/高精动作模仿_2080183256737210370.json, 视频生成/图生视频/高精动作模仿，只模仿动作，1：1复刻动作_2077952800755118081.json, 视频生成/图生视频/高精动作模仿，只模仿动作，1：1复刻动作_2078675405703307266.json, 视频生成/图生视频/高精细1_1复刻动作迁移，动作模仿plus版_2084239498350776322.json, 视频生成/图生视频/高精细1：1复刻动作模仿，动作迁移_2078075351011520514.json, 视频生成/图生视频/高质量动作迁移人物精细 高级强化版_2083007472301858818.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_131

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/【动作迁移】wan22animate_单人版_2098717884812976129.json、视频生成/图生视频/动作迁移_2045891229149302786.json、视频生成/图生视频/跑高精细的用这个动作迁移，动作高仿，需要高显存跑_2056901108127330305.json、视频生成/图生视频/跑高精细的用这个动作迁移，还是这个版本动作模仿的好_2074305725089804289.json、视频生成/图生视频/高精动作模仿 只模仿动作跳舞模仿 1：1复刻动作_2078408880727609346.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：54%

## 共有节点

全部 14 个 workflow 都包含：
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
- `GetNode` —— 13/14 个有
- `MemoryCleaner` —— 13/14 个有
- `SetNode` —— 13/14 个有
- `VRAMReserver` —— 13/14 个有
- `Int` —— 12/14 个有
- `RHHiddenNodes` —— 12/14 个有
- `VHS_LoadVideo` —— 12/14 个有
- `easy cleanGpuUsed` —— 12/14 个有
- `easy showAnything` —— 12/14 个有
- `VHS_LoadVideoFFmpeg` —— 2/14 个有
- `easy int` —— 2/14 个有
- `CM_FloatToInt` —— 1/14 个有
- `CR Text` —— 1/14 个有
- `CreateVideo` —— 1/14 个有
- `ImageConcatMulti` —— 1/14 个有
- `Label (rgthree)` —— 1/14 个有
- `LayerUtility: PurgeVRAM V2` —— 1/14 个有
- `SDPoseOODLoader` —— 1/14 个有
- `SDPoseOODProcessor` —— 1/14 个有
- `SaveVideo` —— 1/14 个有
- `easy promptConcat` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
