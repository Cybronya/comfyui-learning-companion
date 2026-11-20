---
name: unknown_workflow_video_lora_sampler_408
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.820143
common_nodes: [BasicScheduler, CLIPTextEncode, ComfySwitchNode, DualCLIPLoader, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVSeparateAVLatent, LoraLoaderModelOnly, MelBandRoFormerModelLoader, MelBandRoFormerSampler, PreviewAudio, PrimitiveBoolean, SamplerCustom, SetLatentNoiseMask, SolidMask, UNETLoader, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine, VisualizeSigmasKJ]
problems: []
missing: []
members: [图片生成/图生图/ltx2.3导演台_去字幕_短剧视频_漫剧视频_电商视频_多宫格_六宫格_九宫格_自动图生视频_2114997491723759618.json, 平台全量/ltx2.3 精简 电商带货视频生成_2059373645289574401.json, 数字人/数字人/竖屏短剧 多宫格工作流，六宫格 九宫格  全自动 LTX2.3 无字幕_2078050041528406017.json, 视频生成/图生视频/ltx2.3  音频驱动 导演台带货 手动版本  无字幕_2083480997940785154.json, 视频生成/图生视频/ltx2.3 电商带货视频版本 竖屏 去字幕  九宫格 自定义 主播 背景 产品  专业运镜_2073463653397184512.json, 视频生成/图生视频/【商业】ltx2.3 电商带货视频版本 竖屏 去字幕  九宫格 自定义 主播 背景 产品  专业运镜_2071936473150087169.json, 视频生成/图生视频/竖屏短剧 多宫格工作流，六宫格 九宫格  全自动 LTX2.3 无字幕_2066428314536996866.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_408

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/ltx2.3导演台_去字幕_短剧视频_漫剧视频_电商视频_多宫格_六宫格_九宫格_自动图生视频_2114997491723759618.json、平台全量/ltx2.3 精简 电商带货视频生成_2059373645289574401.json、数字人/数字人/竖屏短剧 多宫格工作流，六宫格 九宫格  全自动 LTX2.3 无字幕_2078050041528406017.json、视频生成/图生视频/ltx2.3  音频驱动 导演台带货 手动版本  无字幕_2083480997940785154.json、视频生成/图生视频/ltx2.3 电商带货视频版本 竖屏 去字幕  九宫格 自定义 主播 背景 产品  专业运镜_2073463653397184512.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicScheduler`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `DualCLIPLoader`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `PreviewAudio`
- `PrimitiveBoolean`
- `SamplerCustom`
- `SetLatentNoiseMask`
- `SolidMask`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `VisualizeSigmasKJ`

**可变部分**（部分 workflow 才有）：
- `CS-LTXGridDirector` —— 6/7 个有
- `LoadImage` —— 6/7 个有
- `YusuLTXDirectorGuide` —— 6/7 个有
- `孤海注释` —— 6/7 个有
- `PreviewImage` —— 5/7 个有
- `RHHiddenNodes` —— 5/7 个有
- `RH_RhartImageG2ImageToImage` —— 5/7 个有
- `CR Text Concatenate` —— 4/7 个有
- `ImageRGBChannel` —— 4/7 个有
- `Int` —— 4/7 个有
- `JjkText` —— 4/7 个有
- `LayerColor: Levels` —— 4/7 个有
- `RH_LLMAPI_Pro_Node` —— 4/7 个有
- `RH_Utils` —— 4/7 个有
- `SaveImage` —— 4/7 个有
- `ShowAnything|Mie` —— 4/7 个有
- `TextInput_` —— 4/7 个有
- `easy showAnything` —— 4/7 个有
- `ttN concat` —— 4/7 个有
- `CR Text` —— 2/7 个有
- `Fast Groups Muter (rgthree)` —— 2/7 个有
- `GPTImage2PromptPreview` —— 2/7 个有
- `Preview from image [Crystools]` —— 2/7 个有
- `easy imageSave` —— 2/7 个有
- `AudioCrop` —— 1/7 个有
- `IndexTTS2Run` —— 1/7 个有
- `LTXDirector` —— 1/7 个有
- `LTXDirectorGuide` —— 1/7 个有
- `LoadAudio` —— 1/7 个有
- `MuyeTextEditOutput` —— 1/7 个有
- `PrimitiveStringMultiline` —— 1/7 个有
- `RH_Nano_Banana2_Image2Image` —— 1/7 个有
- `SaveAudio` —— 1/7 个有
- `SaveAudioMP3` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
