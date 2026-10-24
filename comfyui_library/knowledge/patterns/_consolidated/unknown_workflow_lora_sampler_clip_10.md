---
name: unknown_workflow_lora_sampler_clip_10
type: Unknown Workflow
frequency: 30
level: moderate
coverage: 0.8261
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Text, CR Text Concatenate, ConditioningZeroOut, DF_Text_Box, Flux2Scheduler, GH_CropRestore, GH_MaskCropV2, GetImageSize+, GuHaiMaskDetect, KSamplerSelect, LoadImage, LoraLoaderModelOnly, Mask Fill Holes, Mask Invert, RandomNoise, ReferenceLatent, SAM3Segment, SamplerCustomAdvanced, SaveImage, SimpleMath+, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy ifElse, 图像缩放V2_孤海, 孤海-遮罩混合运算, 孤海遮罩分析, 布尔孤海, 数学运算_孤海]
problems: []
missing: []
members: [图片生成/图生图/AI全家福合成工作流｜Klein 9B 双人照片一键影棚合影_2095707972948291586.json, 图片生成/图生图/AI换发型工作流｜Klein 9B 保留五官迁移发型_2095469329272893442.json, 图片生成/图生图/klein-换发型V2_2074386683885346818.json, 图片生成/图生图/klein-换发型V2_2084094645323255810.json, 图片生成/图生图/klein-换发型V2_2087438159603916802.json, 图片生成/图生图/klein-换发型V2_2098976410751823874.json, 图片生成/图生图/klein-换发型V2_2099651775971291138.json, 图片生成/图生图/klein-换发型V2_2099789565820231681.json, 图片生成/图生图/klein-换发型V2_2100045085453934593.json, 图片生成/图生图/klein-换发型_2085914332671602690.json, 图片生成/图生图/klein-换发型_2085929499916591105.json, 图片生成/图生图/klein-换发型换头工作流_2083516868182241281.json, 图片生成/图生图/klein-换发型换头快速出图工作流_2083519896297754626.json, 图片生成/图生图/klein-换发型换头快速出图工作流_2100537441814929409.json, 图片生成/图生图/klein-换发型换头快速出图工作流_2100925704874577922.json, 图片生成/图生图/人物一键换发型_2092299907544739842.json, 图片生成/图生图/头发替换，换发型V2-klein_2096556865206439938.json, 图片生成/图生图/头发替换，换发型V2-klein_2098975987039031298.json, 图片生成/图生图/换发型V2_2103086505047711746.json, 图片生成/图生图/换头发_2086334781276647426.json, 图片生成/图生图/模特人物换发型 换脸 超高相似度_2083710086735810561.json, 图片生成/图生图/模特人物换发型换脸_超高相似度AI写真编辑工作流_2084469036947169282.json, 图片生成/图生图/模特人物换发型换脸_超高相似度AI写真编辑工作流_2084480468417863681.json, 图片生成/图生图/美女换发型_2087002414242160641.json, 图片生成/图生图/美女换发型_2087013365725089794.json, 图片生成/图生图/老孙AI-换发型V2_2085539091504001026.json, 图片生成/图生图/超好用🔥一键换发型_2085262080084631553.json, 图片生成/文生图/换发型_2088083592109977601.json, 图片生成/文生图/换发型_2088155136811163649.json, 数字人/数字人/Klein-换发型V2-优化版_2094598027389530113.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_10

> 由 `engine/knowledge_consolidation` 从 30 个 workflow 归纳得出（图片生成/图生图/AI全家福合成工作流｜Klein 9B 双人照片一键影棚合影_2095707972948291586.json、图片生成/图生图/AI换发型工作流｜Klein 9B 保留五官迁移发型_2095469329272893442.json、图片生成/图生图/klein-换发型V2_2074386683885346818.json、图片生成/图生图/klein-换发型V2_2084094645323255810.json、图片生成/图生图/klein-换发型V2_2087438159603916802.json…）

- **类型**：Unknown Workflow
- **样本数**：30
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 30 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `CR Text Concatenate`
- `ConditioningZeroOut`
- `DF_Text_Box`
- `Flux2Scheduler`
- `GH_CropRestore`
- `GH_MaskCropV2`
- `GetImageSize+`
- `GuHaiMaskDetect`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Mask Fill Holes`
- `Mask Invert`
- `RandomNoise`
- `ReferenceLatent`
- `SAM3Segment`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy ifElse`
- `图像缩放V2_孤海`
- `孤海-遮罩混合运算`
- `孤海遮罩分析`
- `布尔孤海`
- `数学运算_孤海`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 29/30 个有
- `孤海注释` —— 27/30 个有
- `PreviewImage` —— 4/30 个有
- `EmptyImage` —— 3/30 个有
- `easy imageConcat` —— 1/30 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
