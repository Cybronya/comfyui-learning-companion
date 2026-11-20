---
name: image_to_image_lora_sampler_unet_3
type: Image To Image
frequency: 71
level: strong
coverage: 0.88462
common_nodes: [CLIPLoader, GetImageSizeAndCount, Int, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy promptLine, easy seed, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/83yijianduotubendi_2046227606177058818.json, 图片生成/反推提示词/yttyyt2.0_2044094533918531586.json, 图片生成/图生图/3-一键多图_2034596368118980609.json, 图片生成/图生图/Cosmic-RaysX-四宫格分镜图-Qwen-Edit-NextScene-2511_2078850162058944513.json, 图片生成/图生图/Qwen-Edit-NextScene单图多分镜_2010617622429179905.json, 图片生成/图生图/Qwen-Edit图生图+自动多分镜分解_2068881213833699330.json, 图片生成/图生图/Qwen3单图自动生成多分镜，人物画面流畅度超高_2021098631322931201.json, 图片生成/图生图/一键生成分镜-多分镜_2078031683097546753.json, 图片生成/图生图/单图多分镜自动扩写-Qwen-Edit-NextScene-2511-8步_2054094825477165057.json, 图片生成/图生图/单图生成多角度分镜（超还原设定）-Qwen-_2021026711038595074.json, 图片生成/图生图/图生图+多分镜自动-Qwen-Edit-NextScene-2511-8步 (1)_2069683097616084993.json, 图片生成/图生图/图生图+多分镜自动-Qwen-Edit-NextScene-2511-8步 (2)_2072867561611546625.json, 图片生成/图生图/图生图+多分镜自动-Qwen-Edit-NextScene-2511-8步_2058722116450742274.json, 图片生成/图生图/图生图+多分镜自动-Qwen-Edit-NextScene-2511-8步_2062707287965388802.json, 图片生成/图生图/图生图+多分镜自动-Qwen-Edit-NextScene-2511-8步_2064258503673475073.json, 图片生成/图生图/图生图+多分镜自动-Qwen-Edit-NextScene-2511-8步_2064522170612670466.json, 图片生成/图生图/图生图+多分镜自动-Qwen-Edit-NextScene-2511-8步_2066012009971404802.json, 图片生成/图生图/图生图+多分镜自动-Qwen-Edit-NextScene-2511-8步_2067443505907195906.json, 图片生成/图生图/图生图+多分镜自动-Qwen-Edit-NextScene-2511-8步_2067849889744244737.json, 图片生成/图生图/图生图+多分镜自动-Qwen-Edit-NextScene-2511-8步_2069313713567526913.json, 图片生成/图生图/图生图+多分镜自动-Qwen-Edit-NextScene-2511-8步_2072518568503234562.json, 图片生成/图生图/图生图+多分镜自动-Qwen-Edit-NextScene-2511-8步_2072586404466614273.json, 图片生成/图生图/图生图+多分镜自动-Qwen-Edit-NextScene-2511-8步_2074298529807425537.json, 图片生成/图生图/图生图+多分镜自动-Qwen-Edit-NextScene-2511-8步_2074302206433648641.json, 图片生成/图生图/图生图+多分镜自动-Qwen-Edit-NextScene-2511-8步_2074662512028639233.json, 图片生成/图生图/图生图+多分镜自动-Qwen-Edit-NextScene-2511-8步_2075410368490467329.json, 图片生成/图生图/图生图+多分镜自动-Qwen-Edit-NextScene-2511-8步_2077559464600883201.json, 图片生成/图生图/图生图+多分镜自动-Qwen-Edit-NextScene-2511-8步_2080101043647635457.json, 图片生成/图生图/图生图+多分镜自动-Qwen-Edit-NextScene-2511-8步_2082729460989775873.json, 图片生成/图生图/图生图+多分镜自动-Qwen-Edit-NextScene-2511-8步_2086996915299897345.json, 图片生成/图生图/图生图+多分镜自动-Qwen-Edit-NextScene-2511-8步_2087075845130248194.json, 图片生成/图生图/图生图+多分镜自动-Qwen-Edit-NextScene-2511-8步_2087096389795926018.json, 图片生成/图生图/图生图+多分镜自动-Qwen-Edit-NextScene-2511-8步_2090266722866647041.json, 图片生成/图生图/图生图+多分镜自动-Qwen-Edit-NextScene-2511-8步_2090366312576016385.json, 图片生成/图生图/图生图+多分镜自动-Qwen-Edit-NextScene-2511-8步_2090622451712610305.json, 图片生成/图生图/图生图+多分镜自动-Qwen-Edit-NextScene-2511-8步_2092083289711538177.json, 图片生成/图生图/图生图+多分镜自动-Qwen-Edit-NextScene-2511-8步_2092145349128445953.json, 图片生成/图生图/图生图+多分镜自动-Qwen-Edit-NextScene-2511-8步_2092427634247553026.json, 图片生成/图生图/图生图+多分镜自动-Qwen-Edit-NextScene-2511-8步_2092790090375454722.json, 图片生成/图生图/图生图+多分镜自动-Qwen-Edit-NextScene-2511-8步_2094020687513079810.json, 图片生成/图生图/图生图+多分镜自动-Qwen-Edit-NextScene-2511-8步_2094043786144997377.json, 图片生成/图生图/图生图+多分镜自动-Qwen-Edit-NextScene-2511-8步_2094320509440847873.json, 图片生成/图生图/图生图+多分镜自动-Qwen-Edit-NextScene-2511-8步_2094595830400512002.json, 图片生成/图生图/图生图+多分镜自动-Qwen-Edit-NextScene-2511-8步_2094603534292578306.json, 图片生成/图生图/图生图+多分镜自动-Qwen-Edit-NextScene-2511-8步_2094731608736751618.json, 图片生成/图生图/图生图+多分镜自动-Qwen-Edit-NextScene-2511-8步_2097300739348590594.json, 图片生成/图生图/图生图+多分镜自动-Qwen-Edit-NextScene-2511-8步_2099452345053700098.json, 图片生成/图生图/图生图+多分镜自动-Qwen-Edit-NextScene-2511-8步_2099476206281379842.json, 图片生成/图生图/图生图+多分镜自动-Qwen-Edit-NextScene-2511-8步_2107418412778610689.json, 图片生成/图生图/图生图+多分镜自动-Qwen-Edit-NextScene-2511-8步_2107433169149579266.json, 图片生成/图生图/图生图+多分镜自动-Qwen-Edit-NextScene-2511-8步_2109480983622938625.json, 图片生成/图生图/图生图+多分镜自动-Qwen-Edit-NextScene-2511-8步_2113511198829408257.json, 图片生成/图生图/图生图-单图多分镜自动-Qwen-Edit-NextScene-2511-8步_2065023689535606785.json, 图片生成/图生图/图生图风格关键帧_2073414172825706497.json, 图片生成/图生图/生图-单图多分镜-Qwen-Edit-NextScene-2511-8步_1999784555659882497.json, 图片生成/图生图/生图-单图多分镜自动-Qwen-2511-8步_2014130545856356353.json, 图片生成/图生图/生图-单图多分镜自动-Qwen-Edit-NextScene-2511-8步_1980908395203051522.json, 图片生成/图生图/生图-单图多分镜自动-Qwen-Edit-NextScene-2511-8步_2048601546207793154.json, 图片生成/图生图/生图-单图多分镜自动-Qwen-Edit-NextScene-2511-8步。绝妙选择！_2033184363063545858.json, 图片生成/图生图/生图-单图多分镜自动-Qwen-Edit-NextScene-2511-8步。绝妙选择！_2043576924345208834.json, 图片生成/图生图/生图-单图多分镜自动-Qwen-Edit-NextScene-2511-8步。绝妙选择！_2054835516427776001.json, 图片生成/图生图/生图-单图多分镜自动-Qwen-Edit-NextScene-2511-8步。绝妙选择！_2055190376130064385.json, 图片生成/图生图/生图-单图多分镜自动-Qwen-Edit-NextScene-2511-8步。绝妙选择！_2075471290839945218.json, 图片生成/图生图/生图-单图生成固定场景多分镜-Qwen-Edit-2511-8步_1985373272273469442.json, 图片生成/图生图/生图-生成分镜多角度-Qwen-Edit-2509-8步_1985369280818593793.json, 图片生成/图生图/生图-生成分镜多角度-Qwen-Edit-2511-8步_2009655937941905409.json, 图片生成/图生图/自己用：单图生成多分镜_1983059420768808961.json, 图片生成/文生图/图生图+多分镜自动-Qwen-Edit-NextScene-2511-8步_2082660755245195266.json, 图片生成/文生图/图生图+多分镜自动-Qwen-Edit-NextScene-2511-8步_2088143998782369794.json, 图片生成/文生图/图生图+多分镜自动-Qwen-Edit-NextScene-2511-8步_2092053482613338114.json, 视频生成/文生视频/图生图+多分镜自动-Qwen-Edit-NextScene-2511-8步_2068856792473493506.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_3

> 由 `engine/knowledge_consolidation` 从 71 个 workflow 归纳得出（图片生成/反推提示词/83yijianduotubendi_2046227606177058818.json、图片生成/反推提示词/yttyyt2.0_2044094533918531586.json、图片生成/图生图/3-一键多图_2034596368118980609.json、图片生成/图生图/Cosmic-RaysX-四宫格分镜图-Qwen-Edit-NextScene-2511_2078850162058944513.json、图片生成/图生图/Qwen-Edit-NextScene单图多分镜_2010617622429179905.json…）

- **类型**：Image To Image
- **样本数**：71
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 71 个 workflow 都包含：
- `CLIPLoader`
- `GetImageSizeAndCount`
- `Int`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy promptLine`
- `easy seed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ProcessString` —— 69/71 个有
- `StringFunction|pysssss` —— 69/71 个有
- `CR Prompt Text` —— 68/71 个有
- `FluxKontextMultiReferenceLatentMethod` —— 68/71 个有
- `RH_LLMAPI_NODE` —— 68/71 个有
- `ImageListToBatch+` —— 67/71 个有
- `PrimitiveStringMultiline` —— 67/71 个有
- `easy saveText` —— 67/71 个有
- `FL_ImageBatchToGrid` —— 66/71 个有
- `CM_FloatToInt` —— 65/71 个有
- `CM_FloatUnaryOperation` —— 65/71 个有
- `CM_IntToFloat` —— 65/71 个有
- `CFGNorm` —— 64/71 个有
- `ModelSamplingAuraFlow` —— 64/71 个有
- `Qwen3_VQA_Plus` —— 64/71 个有
- `JWIntegerToString` —— 63/71 个有
- `ImageConcatMulti` —— 4/71 个有
- `PreviewImage` —— 4/71 个有
- `ConditioningZeroOut` —— 3/71 个有
- `RTXVideoSuperResolution` —— 2/71 个有
- `Text Multiline` —— 2/71 个有
- `ShowText|pysssss` —— 1/71 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 71 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 71 | 100% |
| 采样算法 | euler | - | 71 | 100% |
| 调度器 | simple | - | 71 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 71 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 71/71 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，71 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，71 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，71 个样本，一致性 100%
- 调度器 最常用 simple，71 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，71 个样本，取值集中（一致性 100%）
- 高发问题（71/71 个样本）：Steps较低可能导致细节不足
