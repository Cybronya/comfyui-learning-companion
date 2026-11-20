---
name: image_to_image_sampler_clip_unet_43
type: Image To Image
frequency: 11
level: strong
coverage: 0.943091
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [平台全量/Kontext快速出图comfyui物品迁移_1940393934617030657.json, 平台全量/flux kontext多图合成_1944743285359300609.json, 平台全量/flux kontext真人转吉卜力风格_1941662342616924161.json, 平台全量/flux kontext线稿转效果图_1942221589012484098.json, 平台全量/flux-kontext-dev官方工作流_1938576045555507202.json, 平台全量/flux1图生图工作流_2117132770823729154.json, 平台全量/kontext一键打光lora工作流_1941442117841612802.json, 平台全量/扩图  kontext_1950897398702866434.json, 平台全量/美妆精修(包装盒)_1962391840064409602.json, 平台全量/美妆精修(金属材质)_1961592020294942722.json, 平台全量/美妆精修（透明材质）_1955591299962322945.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_43

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（平台全量/Kontext快速出图comfyui物品迁移_1940393934617030657.json、平台全量/flux kontext多图合成_1944743285359300609.json、平台全量/flux kontext真人转吉卜力风格_1941662342616924161.json、平台全量/flux kontext线稿转效果图_1942221589012484098.json、平台全量/flux-kontext-dev官方工作流_1938576045555507202.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 10/11 个有
- `ReferenceLatent` —— 10/11 个有
- `FluxKontextImageScale` —— 9/11 个有
- `LoraLoaderModelOnly` —— 8/11 个有
- `ImageConcanate` —— 5/11 个有
- `ImageStitch` —— 5/11 个有
- `PreviewImage` —— 5/11 个有
- `easy cleanGpuUsed` —— 3/11 个有
- `EmptySD3LatentImage` —— 2/11 个有
- `ImagePadForOutpaint` —— 2/11 个有
- `CR Prompt Text` —— 1/11 个有
- `ImageConcatMulti` —— 1/11 个有
- `ImageResize+` —— 1/11 个有
- `ImageScale` —— 1/11 个有
- `RH_Translator` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 11 | 86% |
| Prompt 约束强度(CFG) | 1 | 0.85 - 1 | 11 | 96% |
| 采样算法 | euler | - | 11 | 91% |
| 调度器 | simple | - | 11 | 55% |
| 重绘幅度 | 1 | 0.5 - 1 | 11 | 85% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，11 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 0.85 - 1，11 个样本，取值集中（一致性 96%）
- 采样算法 最常用 euler，11 个样本，一致性 91%
- 调度器 最常用 simple，11 个样本，一致性 55%
- 重绘幅度 中位数 1，观测区间 0.5 - 1，11 个样本，取值集中（一致性 85%）
- 风险：Prompt 约束强度(CFG) 观测到 0.85，低于常用下限 1（CFG 过低可能导致 Prompt 约束不足、结果偏离描述）
