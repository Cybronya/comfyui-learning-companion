---
name: image_to_image_lora_sampler_clip_31
type: Image To Image
frequency: 10
level: strong
coverage: 0.9062
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/CHEN-F.1-Kontext-极限电商换装V2_1958766766275059713.json, 平台全量/Kontext+lora图片编辑工作流（自行选择lora）_1943122590053654529.json, 平台全量/Kontext+lora模型使用_1942005088108101633.json, 平台全量/kontext  dev 图像编辑_1938438501795037185.json, 平台全量/kontext人像精修_1950175952473120770.json, 平台全量/kontext金属产品精修_1947337375380819969.json, 平台全量/模特换衣-kontext_1959310057420828673.json, 平台全量/真实照片转3D动漫（参考背景）_1948411129983840258.json, 平台全量/真实照片转3D动漫（自动润色背景）_1948346175886884866.json, 平台全量/转换成刺绣风格_1948967719677435906.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_31

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（平台全量/CHEN-F.1-Kontext-极限电商换装V2_1958766766275059713.json、平台全量/Kontext+lora图片编辑工作流（自行选择lora）_1943122590053654529.json、平台全量/Kontext+lora模型使用_1942005088108101633.json、平台全量/kontext  dev 图像编辑_1938438501795037185.json、平台全量/kontext人像精修_1950175952473120770.json…）

- **类型**：Image To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `RH_Translator` —— 8/10 个有
- `CR Text` —— 7/10 个有
- `PreviewImage` —— 7/10 个有
- `easy cleanGpuUsed` —— 6/10 个有
- `CR Text Concatenate` —— 5/10 个有
- `ShowText|pysssss` —— 5/10 个有
- `Anything Everywhere3` —— 3/10 个有
- `ImageStitch` —— 3/10 个有
- `RH_Captioner` —— 3/10 个有
- `ImagePadForOutpaint` —— 2/10 个有
- `TeaCache` —— 2/10 个有
- `ttN concat` —— 2/10 个有
- `Switch image [Crystools]` —— 1/10 个有
- `Text Multiline` —— 1/10 个有
- `easy float` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 9 - 30 | 10 | 73% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 9 - 30，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
