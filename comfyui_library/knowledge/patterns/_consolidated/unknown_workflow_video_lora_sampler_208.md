---
name: unknown_workflow_video_lora_sampler_208
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.952333
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, ImageBatchExtendWithOverlap, JWInteger, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, VAEDecode, VAELoader, VHS_VideoCombine, easy forLoopEnd, easy forLoopStart, easy promptLine]
problems: []
missing: []
members: [视频生成/图生视频/3.生视频类-6..真人、动漫、跳舞长视频001.长视频-手动-真人&动漫.json_2022090916130988033.json, 视频生成/图生视频/SVI 2 Pro长视频循环动态版V1.0_2005998489748328449.json, 视频生成/图生视频/Wan 2.2 Remix2.1 + SVI2 Pro：超丝滑长视频生成+精准叙事_2011456654914621441.json, 视频生成/图生视频/Wan 2.2 Remix2.1 + SVI2 Pro：超丝滑长视频生成+精准叙事（确实很不错）_2043277344625926145.json, 视频生成/图生视频/Wan 2.2 Remix2.1图生长视频 ：分镜时长+精准叙事_2016438828810117122.json, 视频生成/图生视频/【4月】Wan2.2 Dasiwa V10+ SVI2Pro全自动长视频（严格遵循提示词控制）_2042934269093355522.json, 视频生成/图生视频/视频：20s长视频剧情生成_2035685146686394370.json, 视频生成/图生视频/🔥超丝滑长视频生成-分镜时长+内容定制精准叙事_2046827963190087682.json, 视频生成/文生视频/Wan 2.2 Remix2.1 + SVI2 Pro：超丝滑长视频生成+精准叙事_2047624351276601345.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_208

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/3.生视频类-6..真人、动漫、跳舞长视频001.长视频-手动-真人&动漫.json_2022090916130988033.json、视频生成/图生视频/SVI 2 Pro长视频循环动态版V1.0_2005998489748328449.json、视频生成/图生视频/Wan 2.2 Remix2.1 + SVI2 Pro：超丝滑长视频生成+精准叙事_2011456654914621441.json、视频生成/图生视频/Wan 2.2 Remix2.1 + SVI2 Pro：超丝滑长视频生成+精准叙事（确实很不错）_2043277344625926145.json、视频生成/图生视频/Wan 2.2 Remix2.1图生长视频 ：分镜时长+精准叙事_2016438828810117122.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ImageBatchExtendWithOverlap`
- `JWInteger`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy promptLine`

**可变部分**（部分 workflow 才有）：
- `DiffusionModelLoaderKJ` —— 8/9 个有
- `VAEEncode` —— 8/9 个有
- `WanImageToVideoSVIPro` —— 8/9 个有
- `DF_Int_to_Float` —— 6/9 个有
- `GODMT_ListGetByIndex` —— 6/9 个有
- `GODMT_SplitString` —— 6/9 个有
- `MathExpression|pysssss` —— 6/9 个有
- `StringToInt` —— 6/9 个有
- `WWAA-LineCount` —— 6/9 个有
- `Int` —— 3/9 个有
- `SimpleMath+` —— 3/9 个有
- `ModelSamplingSD3` —— 1/9 个有
- `RIFE VFI` —— 1/9 个有
- `UNETLoader` —— 1/9 个有
- `WanAdvancedI2V` —— 1/9 个有
- `easy float` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 9 | 67% |
| Prompt 约束强度(CFG) | 8 | 6 - 8 | 9 | 92% |
| 采样算法 | 1 | 1 - 1 | 9 | 100% |
| 调度器 | euler | - | 9 | 100% |
| 重绘幅度 | simple | - | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，9 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 8，观测区间 6 - 8，9 个样本，取值集中（一致性 92%）
- 采样算法 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，9 个样本，一致性 100%
- 重绘幅度 最常用 simple，9 个样本，一致性 100%
