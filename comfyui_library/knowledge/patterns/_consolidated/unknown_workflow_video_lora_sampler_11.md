---
name: unknown_workflow_video_lora_sampler_11
type: Unknown Workflow
frequency: 45
level: strong
coverage: 0.874556
common_nodes: [Any To Any, BerniniConditioning, CLIPLoader, CLIPTextEncode, CR Prompt Text, Float, HunyuanVideoFoley, Int, JWInteger, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PathchSageAttentionKJ, Qwen3_VQA, Text, UNETLoader, VAEDecode, VAELoader, VHS_SelectFilename, VHS_VideoCombine, easy cleanGpuUsed, easy mathInt, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/bernini上传多参分镜自动扩展提示词_2085579405052698626.json, 视频生成/图生视频/bernini上传多参分镜自动扩展提示词_2085605535533068290.json, 视频生成/图生视频/2079216311300878337.json, 视频生成/图生视频/2076678007443509249.json, 视频生成/图生视频/2079559170201837570.json, 视频生成/图生视频/2076486473653776385.json, 视频生成/图生视频/2077297515594076162.json, 视频生成/图生视频/2076302783288008706.json, 视频生成/图生视频/2081017151829397505.json, 视频生成/图生视频/2081212413805940737.json, 视频生成/图生视频/2080456381441859585.json, 视频生成/图生视频/2080483813427343362.json, 视频生成/图生视频/2080457429132857345.json, 视频生成/图生视频/2080516332377952258.json, 视频生成/图生视频/叮叮的飞吻_2083468110757187585.json, 视频生成/图生视频/周末愉快_2083807638411894785.json, 视频生成/图生视频/哈哈，好看的裙子，哈哈，很有曲线美_2083501855832895490.json, 视频生成/图生视频/2081230151186210817.json, 视频生成/图生视频/2080522658558595074.json, 视频生成/图生视频/2081243950228267010.json, 视频生成/图生视频/2080891153406316545.json, 视频生成/图生视频/2080857100208664577.json, 视频生成/图生视频/2080244665965699073.json, 视频生成/图生视频/2079557430773637122.json, 视频生成/图生视频/2077431585602891778.json, 视频生成/图生视频/2077420333774237698.json, 视频生成/图生视频/2077430810310955010.json, 视频生成/图生视频/漫剧俯拍长镜头_2083497022388269057.json, 视频生成/图生视频/2081693338629140481.json, 视频生成/图生视频/2077710494714130434.json, 视频生成/图生视频/2079571585241014274.json, 视频生成/图生视频/2079963275604877314.json, 视频生成/图生视频/2080167337260568577.json, 视频生成/图生视频/2080203702916444161.json, 视频生成/图生视频/2080262167093399553.json, 视频生成/图生视频/2080279967212064769.json, 视频生成/图生视频/漫剧长镜头图书馆场景_2083527540001566722.json, 视频生成/图生视频/漫剧风格化图像转视频_2083521242224750594.json, 视频生成/图生视频/电商商品拍摄TEST1_2083809381015187458.json, 视频生成/图生视频/电商商品拍摄TEST2_2083816642307514369.json, 视频生成/图生视频/电商商品拍摄TEST3_2083816654127067138.json, 视频生成/图生视频/2077445647162236930.json, 视频生成/图生视频/高动态漫剧图生视频1_2082704275330920450.json, 视频生成/图生视频/高动态漫剧图生视频_2082719576378400770.json, 视频生成/图生视频/高动态漫剧图生视频_2082730576058081281.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_11

> 由 `engine/knowledge_consolidation` 从 45 个 workflow 归纳得出（视频生成/图生视频/bernini上传多参分镜自动扩展提示词_2085579405052698626.json、视频生成/图生视频/bernini上传多参分镜自动扩展提示词_2085605535533068290.json、视频生成/图生视频/2079216311300878337.json、视频生成/图生视频/2076678007443509249.json、视频生成/图生视频/2079559170201837570.json…）

- **类型**：Unknown Workflow
- **样本数**：45
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 45 个 workflow 都包含：
- `Any To Any`
- `BerniniConditioning`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `Float`
- `HunyuanVideoFoley`
- `Int`
- `JWInteger`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `Qwen3_VQA`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_SelectFilename`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy mathInt`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `RH_Captioner` —— 39/45 个有
- `TextConcatenate_UTK` —— 39/45 个有
- `PreviewImage` —— 33/45 个有
- `RH_Translator` —— 26/45 个有
- `GoogleTranslateTextNode` —— 13/45 个有
- `ImageResizeKJv2` —— 12/45 个有
- `ImageConcatMulti` —— 11/45 个有
- `ImageConcatenate_UTK` —— 9/45 个有
- `JDCN_StringToList` —— 9/45 个有
- `StringReplace` —— 9/45 个有
- `easy indexAnything` —— 9/45 个有
- `RHHiddenNodes` —— 6/45 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 45 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 45 | 100% |
| 采样算法 | 1 | 1 - 1 | 45 | 100% |
| 调度器 | euler | - | 45 | 100% |
| 重绘幅度 | simple | - | 45 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，45 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，45 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，45 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，45 个样本，一致性 100%
- 重绘幅度 最常用 simple，45 个样本，一致性 100%
