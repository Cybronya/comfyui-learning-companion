---
name: unknown_workflow_video_lora_sampler_12
type: Unknown Workflow
frequency: 46
level: moderate
coverage: 0.5145
common_nodes: [CLIPVisionLoader, ImageResizeKJv2, Int, LoadImage, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/2017562279276974081.json, 视频生成/图生视频/2019075587062636545.json, 视频生成/图生视频/2073705930453245954.json, 视频生成/图生视频/2017135847610519553.json, 视频生成/图生视频/2003473617683922946.json, 视频生成/图生视频/2006380310623162369.json, 视频生成/图生视频/2053406061868138498.json, 视频生成/图生视频/2007482787619672065.json, 视频生成/图生视频/2017109030061219842.json, 视频生成/图生视频/2062344581278158849.json, 视频生成/图生视频/2057669238491537409.json, 视频生成/图生视频/changge zhufu_2094680904781352962.json, 视频生成/图生视频/greeting video_2089174015540817921.json, 视频生成/图生视频/2033034553987702785.json, 视频生成/图生视频/2057856312750465025.json, 视频生成/图生视频/2020604766358872065.json, 视频生成/图生视频/一键生成超精细动作迁移 单双人舞蹈动作模仿 各种动作复刻参考图生视频_2087865873062256642.json, 视频生成/图生视频/2046484614713188353.json, 视频生成/图生视频/人物精细高质量动作迁移 复刻动作 高级强化版_2083510108717408257.json, 视频生成/图生视频/人物精细高质量动作迁移 复刻动作 高级强化版_2083521883307339778.json, 视频生成/图生视频/人物精细高质量动作迁移 高级强化版_2083363876598534146.json, 视频生成/图生视频/2078312802099482626.json, 视频生成/图生视频/2039672616482508802.json, 视频生成/图生视频/2039992227572748290.json, 视频生成/图生视频/动作迁移(超能抖)+随意调节+动作复刻_2109524936074293249.json, 视频生成/图生视频/2040075523052802049.json, 视频生成/图生视频/2047655725190619137.json, 视频生成/图生视频/2042165206326976513.json, 视频生成/图生视频/2056034376437256194.json, 视频生成/图生视频/2056388313015209985.json, 视频生成/图生视频/2058520279621652482.json, 视频生成/图生视频/2059247790496243714.json, 视频生成/图生视频/2070370786665385985.json, 视频生成/图生视频/2071503643160956929.json, 视频生成/图生视频/2078450483810889729.json, 视频生成/图生视频/2078647438625300482.json, 视频生成/图生视频/2082351326247350274.json, 视频生成/图生视频/动作迁移【可抖X】_2030874906992320514.json, 视频生成/图生视频/2039672522324582401.json, 视频生成/图生视频/动作迁移【可抖X】清晰-好-6秒300RH_2082825993336745985.json, 视频生成/图生视频/2036032896015802370.json, 视频生成/图生视频/动作迁移抖胸设置动作高仿舞蹈复刻模仿角色替换人物替换_2092861283463950338.json, 视频生成/图生视频/2033570281733758977.json, 视频生成/图生视频/2060615103225094145.json, 视频生成/图生视频/口哨舞-动作迁移_2089255191454502914.json, 视频生成/图生视频/唱歌30秒_2099739134943391746.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_12

> 由 `engine/knowledge_consolidation` 从 46 个 workflow 归纳得出（视频生成/图生视频/2017562279276974081.json、视频生成/图生视频/2019075587062636545.json、视频生成/图生视频/2073705930453245954.json、视频生成/图生视频/2017135847610519553.json、视频生成/图生视频/2003473617683922946.json…）

- **类型**：Unknown Workflow
- **样本数**：46
- **可信度**：中等可信
- **平均知识覆盖**：51%

## 共有节点

全部 46 个 workflow 都包含：
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `Int`
- `LoadImage`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `BatchCount+` —— 45/46 个有
- `GetNode` —— 45/46 个有
- `ImageBatch` —— 45/46 个有
- `ImageFromBatch` —— 45/46 个有
- `PoseAndFaceDetection` —— 45/46 个有
- `RepeatImageBatch` —— 45/46 个有
- `SetNode` —— 45/46 个有
- `easy mathInt` —— 45/46 个有
- `PreviewImage` —— 44/46 个有
- `RHHiddenNodes` —— 44/46 个有
- `DrawViTPose` —— 40/46 个有
- `OnnxDetectionModelLoader` —— 40/46 个有
- `WanVideoModelLoader` —— 39/46 个有
- `WanVideoLoraSelectMulti` —— 38/46 个有
- `WanVideoContextOptions` —— 37/46 个有
- `WanVideoLoraSelect` —— 37/46 个有
- `VRAMReserver` —— 36/46 个有
- `easy float` —— 36/46 个有
- `easy showAnything` —— 35/46 个有
- `MemoryCleaner` —— 16/46 个有
- `LazySwitch1way` —— 7/46 个有
- `WanVideoTeaCache` —— 7/46 个有
- `easy compare` —— 7/46 个有
- `孤海注释` —— 3/46 个有
- `ComfyMathExpression` —— 2/46 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/46 个有
- `Primitive integer [Crystools]` —— 2/46 个有
- `SimpleMath+` —— 2/46 个有
- `easy int` —— 2/46 个有
- `FlashVSRNode` —— 1/46 个有
- `GemmaAPITextEncode` —— 1/46 个有
- `GetImageSize+` —— 1/46 个有
- `GetImageSizeAndCount` —— 1/46 个有
- `ImageScale` —— 1/46 个有
- `ImageUpscaleWithModel` —— 1/46 个有
- `MathExpression|pysssss` —— 1/46 个有
- `UpscaleModelLoader` —— 1/46 个有
- `WanVideoEasyCache` —— 1/46 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
