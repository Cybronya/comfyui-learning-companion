---
name: text_to_image_sampler_clip_unet_10
type: Text To Image
frequency: 19
level: strong
coverage: 0.673895
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, PreviewAny, PrimitiveStringMultiline, SaveImage, StringConcatenate, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2 Turbo文生图(wlop）lora_2070665195122413570.json, 图片生成/文生图/Krea2 Turbo文生图+全节点注释_2072663092810575873.json, 图片生成/文生图/Krea2 Turbo文生图V1_2069662522738831362.json, 图片生成/文生图/Krea2 Turbo文生图V1_2070018860480286722.json, 图片生成/文生图/Krea2-Turbo-文生图_2069949151932149761.json, 图片生成/文生图/Krea2_turbo_文生图_2066148990659416066.json, 图片生成/文生图/Krea2_turbo基础工作流（官方版本构架微调）_2083013364665643010.json, 图片生成/文生图/Krea2文生图+提示词反推Turbo+Realism+Engineer+V2_2072569695793926145.json, 图片生成/文生图/image_krea2_turbo_t2i_2069968212200087553.json, 图片生成/文生图/image_krea2_turbo_t2i_2072904099296800770.json, 图片生成/文生图/image_krea2_turbo_t2i_2079183226878382082.json, 图片生成/文生图/image_krea2_turbo文生图_2074494308316700673.json, 图片生成/文生图/krea2_turbo_t2i_api_2098965323885146113.json, 图片生成/文生图/图图小脸蛋 KREA2 工作流_2072299896564178946.json, 图片生成/文生图/图图的标准KREA2 TURBO 工作流（附带官方提示词优化功能）_2070019455769473025.json, 图片生成/文生图/（Zhen style风格模型）Krea2 Turbo文生图V1_2071136461566599169.json, 图片生成/文生图/（图图版）Krea2 Turbo文生图V1_2072524020372828162.json, 图片生成/文生图/（贞贞版-Raw Lora 1000步）Krea2 Turbo文生图V1_2073809636901351425.json, 图片生成/文生图/（贞贞版）Krea2 Turbo文生图V1_2070539771801325570.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_10

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/文生图/Krea2 Turbo文生图(wlop）lora_2070665195122413570.json、图片生成/文生图/Krea2 Turbo文生图+全节点注释_2072663092810575873.json、图片生成/文生图/Krea2 Turbo文生图V1_2069662522738831362.json、图片生成/文生图/Krea2 Turbo文生图V1_2070018860480286722.json、图片生成/文生图/Krea2-Turbo-文生图_2069949151932149761.json…）

- **类型**：Text To Image
- **样本数**：19
- **可信度**：强结论
- **平均知识覆盖**：67%

## 共有节点

全部 19 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `SaveImage`
- `StringConcatenate`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 18/19 个有
- `LoraLoaderModelOnly` —— 16/19 个有
- `ResolutionSelector` —— 15/19 个有
- `ComfySwitchNode` —— 8/19 个有
- `PrimitiveBoolean` —— 8/19 个有
- `CR Prompt Text` —— 5/19 个有
- `TextConcat` —— 5/19 个有
- `LoadImage` —— 3/19 个有
- `Int` —— 2/19 个有
- `CR Text` —— 1/19 个有
- `Fast Groups Bypasser (rgthree)` —— 1/19 个有
- `PreviewImage` —— 1/19 个有
- `RH_Captioner` —— 1/19 个有
- `easy promptLine` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 10 | 19 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 19 | 100% |
| 采样算法 | euler | - | 19 | 100% |
| 调度器 | simple | - | 19 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 19 | 100% |
| 宽度 | 1024 | 1024 - 2048 | 19 | 72% |
| 高度 | 1024 | 1024 - 2048 | 19 | 72% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/19 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 10，19 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，19 个样本，一致性 100%
- 调度器 最常用 simple，19 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 2048，19 个样本
- 高度 中位数 1024，观测区间 1024 - 2048，19 个样本
- 高发问题（14/19 个样本）：Steps较低可能导致细节不足
