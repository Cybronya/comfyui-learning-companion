---
name: unknown_workflow_lora_sampler_vae_2
type: Unknown Workflow
frequency: 25
level: strong
coverage: 0.9062
common_nodes: [CLIPLoader, ConditioningZeroOut, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/Qwen-image-Edit-2509_丰胸_2003293711083700226.json, 平台全量/一键换装_2087704085607829505.json, 平台全量/换装 换衣  服装展示   FireRed-Image-Edit_2117666220249018370.json, 平台全量/换装 换衣  服装展示   FireRed-Image-Edit_2118247895441956865.json, 平台全量/换装 换衣  电商服装展示  小红书  FireRed-Image-Edit_2109580075048980482.json, 平台全量/换装 换衣  电商服装展示  小红书  FireRed-Image-Edit_2109873007299751938.json, 平台全量/换装 换衣  电商服装展示  小红书  FireRed-Image-Edit_2112418082789613570.json, 平台全量/换装 换衣  电商服装展示  小红书  FireRed-Image-Edit_2117206371375603713.json, 平台全量/换装 换衣  电商服装展示  小红书  FireRed-Image-Edit_2117220857025220609.json, 平台全量/换装 换衣  电商服装展示  小红书  FireRed-Image-Edit_2117228142464159746.json, 平台全量/换装 换衣  电商服装展示  小红书  FireRed-Image-Edit_2117228377739452418.json, 平台全量/换装 换衣  电商服装展示  小红书  FireRed-Image-Edit_2117294372566945793.json, 平台全量/换装 换衣  电商服装展示  小红书  FireRed-Image-Edit_2117297662126026754.json, 平台全量/换装 换衣  电商服装展示  小红书  FireRed-Image-Edit_2117297948311769089.json, 平台全量/换装 换衣  电商服装展示  小红书  FireRed-Image-Edit_2117584015518691330.json, 平台全量/换装 换衣  电商服装展示  小红书  FireRed-Image-Edit_2117584487952502786.json, 平台全量/换装 换衣  电商服装展示  小红书  FireRed-Image-Edit_2117584946536730626.json, 平台全量/换装 换衣  电商服装展示  小红书  FireRed-Image-Edit_2117679143562338305.json, 平台全量/换装 换衣  电商服装展示  小红书  FireRed-Image-Edit_2117684770636394497.json, 平台全量/换装 换衣  电商服装展示  小红书  FireRed-Image-Edit_2117853459096621057.json, 平台全量/换装 换衣  电商服装展示  小红书  FireRed-Image-Edit_2117961589952442369.json, 平台全量/换装 换衣  电商服装展示  小红书  FireRed-Image-Edit_2118208189857615873.json, 平台全量/换装 换衣  电商服装展示  小红书  FireRed-Image-Edit_2118222921226346497.json, 平台全量/换装 换衣  电商服装展示  小红书  FireRed-Image-Edit_2118303460184645633.json, 平台全量/电商参考图片生成文字海报 FireRed_2030452986723442690.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_vae_2

> 由 `engine/knowledge_consolidation` 从 25 个 workflow 归纳得出（平台全量/Qwen-image-Edit-2509_丰胸_2003293711083700226.json、平台全量/一键换装_2087704085607829505.json、平台全量/换装 换衣  服装展示   FireRed-Image-Edit_2117666220249018370.json、平台全量/换装 换衣  服装展示   FireRed-Image-Edit_2118247895441956865.json、平台全量/换装 换衣  电商服装展示  小红书  FireRed-Image-Edit_2109580075048980482.json…）

- **类型**：Unknown Workflow
- **样本数**：25
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 25 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 24/25 个有
- `PreviewImage` —— 23/25 个有
- `PIP_图像联结` —— 22/25 个有
- `Image Comparer (rgthree)` —— 3/25 个有
- `Anything Everywhere` —— 1/25 个有
- `GetNode` —— 1/25 个有
- `JjkShowText` —— 1/25 个有
- `RH_Captioner_Pro` —— 1/25 个有
- `UnetLoaderGGUF` —— 1/25 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 25 | 81% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 25 | 100% |
| 采样算法 | euler | - | 25 | 96% |
| 调度器 | simple | - | 25 | 92% |
| 重绘幅度 | 1 | 1 - 1 | 25 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 25/25 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，25 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，25 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，25 个样本，一致性 96%
- 调度器 最常用 simple，25 个样本，一致性 92%
- 重绘幅度 中位数 1，观测区间 1 - 1，25 个样本，取值集中（一致性 100%）
- 高发问题（25/25 个样本）：Steps较低可能导致细节不足
