---
name: unknown_workflow_video_lora_sampler_221
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.604667
common_nodes: [Any To Any, Any To String (mtb), CLIPLoader, CLIPTextEncode, CR Prompt Text, CR Text Concatenate, DiffusionModelLoaderKJ, GODMT_SplitString, GetNode, INTConstant, ImageListToBatch+, ImageResizeKJv2, ImpactInt, IndexTTS2Run, Int, JjkText, KSamplerAdvanced, LoadAudio, LoadImage, LoraLoaderModelOnly, RH_GetAudioDuration, SDVM Image List Repeat, SaveAudio, SetNode, SimpleMath+, Text List Concatenate, TextListSelelct, ToInt, VAEDecode, VAEEncode, VAELoader, VHS_SelectImages, VHS_VideoCombine, WanImageToVideoSVIPro, easy cleanGpuUsed, easy forLoopEnd, easy forLoopStart, easy lengthAnything, easy promptList, easy showAnything, seed _O]
problems: []
missing: []
members: [视频生成/图生视频/WAN2.2+SVI2.0PRO五分镜长视频+旁白声音_2036666010664706050.json, 视频生成/图生视频/一分半解说短剧WAN2.2REMIX3+SVI2.0PRO+VBVR十二图片长视频_2046443444645662722.json, 视频生成/图生视频/一分钟旁白短剧首选WAN2.2+SVI2.0PRO十图片生成长视频+生成旁白声音_2012066025520504833.json, 视频生成/图生视频/一分钟旁白短剧首选WAN2.2+SVI2.0PRO十图片生成长视频+生成旁白声音_2013826587573096449.json, 视频生成/图生视频/一分钟旁白短剧首选WAN2.2+SVI2.0PRO十图片生成长视频+生成旁白声音_2014173118008401922.json, 视频生成/图生视频/一分钟旁白短剧首选加速稳定版十段视频WAN2.2+SVI2.0PRO十图片生成长视频+生成旁白声音_2016043125470404609.json, 视频生成/图生视频/一分钟旁白短剧首选稳定版十段视频WAN2.2+SVI2.0PRO十图片生成长视频+生成旁白声音_2015670152976670722.json, 视频生成/文生视频/一分钟旁白短剧首选WAN2.2+SVI2.0PRO十图片生成长视频+生成旁白声音_2015056410270244865.json, 视频生成/文生视频/一分钟旁白短剧首选稳定版十段视频WAN2.2+SVI2.0PRO十图片生成长视频+生成旁白声音_2049176470618120194.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_221

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/WAN2.2+SVI2.0PRO五分镜长视频+旁白声音_2036666010664706050.json、视频生成/图生视频/一分半解说短剧WAN2.2REMIX3+SVI2.0PRO+VBVR十二图片长视频_2046443444645662722.json、视频生成/图生视频/一分钟旁白短剧首选WAN2.2+SVI2.0PRO十图片生成长视频+生成旁白声音_2012066025520504833.json、视频生成/图生视频/一分钟旁白短剧首选WAN2.2+SVI2.0PRO十图片生成长视频+生成旁白声音_2013826587573096449.json、视频生成/图生视频/一分钟旁白短剧首选WAN2.2+SVI2.0PRO十图片生成长视频+生成旁白声音_2014173118008401922.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：60%

## 共有节点

全部 9 个 workflow 都包含：
- `Any To Any`
- `Any To String (mtb)`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `CR Text Concatenate`
- `DiffusionModelLoaderKJ`
- `GODMT_SplitString`
- `GetNode`
- `INTConstant`
- `ImageListToBatch+`
- `ImageResizeKJv2`
- `ImpactInt`
- `IndexTTS2Run`
- `Int`
- `JjkText`
- `KSamplerAdvanced`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RH_GetAudioDuration`
- `SDVM Image List Repeat`
- `SaveAudio`
- `SetNode`
- `SimpleMath+`
- `Text List Concatenate`
- `TextListSelelct`
- `ToInt`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_SelectImages`
- `VHS_VideoCombine`
- `WanImageToVideoSVIPro`
- `easy cleanGpuUsed`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy lengthAnything`
- `easy promptList`
- `easy showAnything`
- `seed _O`

**可变部分**（部分 workflow 才有）：
- `ImageBatch` —— 6/9 个有
- `Display Any (rgthree)` —— 3/9 个有
- `AudioAdjustVolume` —— 1/9 个有
- `ConcatTextOfUtils` —— 1/9 个有
- `HunyuanVideoFoley` —— 1/9 个有
- `ImageSizeInfo` —— 1/9 个有
- `JWStringGetLine` —— 1/9 个有
- `PathchSageAttentionKJ` —— 1/9 个有
- `RH_Translator` —— 1/9 个有
- `ResizeImagesByLongerEdge` —— 1/9 个有
- `TextBox` —— 1/9 个有
- `llama_cpp_instruct_adv` —— 1/9 个有
- `llama_cpp_model_loader` —— 1/9 个有
- `llama_cpp_parameters` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 9 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 9 | 100% |
| 采样算法 | 2 | 1.8 - 2 | 9 | 97% |
| 调度器 | euler | - | 9 | 100% |
| 重绘幅度 | simple | - | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，9 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，9 个样本，取值集中（一致性 100%）
- 采样算法 中位数 2，观测区间 1.8 - 2，9 个样本，取值集中（一致性 97%）
- 调度器 最常用 euler，9 个样本，一致性 100%
- 重绘幅度 最常用 simple，9 个样本，一致性 100%
