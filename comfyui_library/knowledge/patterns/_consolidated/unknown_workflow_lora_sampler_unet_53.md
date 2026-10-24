---
name: unknown_workflow_lora_sampler_unet_53
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.9108
common_nodes: [CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/【LG】QWEN2511极简极低偏移换装_2004542473714237441.json, 图片生成/图生图/动漫光斑光影增强_qwen 2511_2025486195010052098.json, 图片生成/图生图/史上最强-小红书动漫转写实真人_2043235575892807682.json, 图片生成/图生图/史上最强-小红书动漫转写实真人（FireRed_OmniRealism）_2037918131322101761.json, 图片生成/图生图/史上最强-小红书动漫转写实真人（FireRed_OmniRealism）_2038424926553640962.json, 图片生成/图生图/小红书FireRed-Image-Edit1.1（单图、双图、三图编辑）_2029922206393831425.json, 图片生成/图生图/小红书_动漫转写实真人_2083827042285604866.json, 图片生成/图生图/小红书模型动漫转真人_2067301137937686530.json, 图片生成/图生图/涂鸦控制_海报设计_2026556702794977281.json, 图片生成/图生图/涂鸦控制_海报设计_2026672287650418690.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_53

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/【LG】QWEN2511极简极低偏移换装_2004542473714237441.json、图片生成/图生图/动漫光斑光影增强_qwen 2511_2025486195010052098.json、图片生成/图生图/史上最强-小红书动漫转写实真人_2043235575892807682.json、图片生成/图生图/史上最强-小红书动漫转写实真人（FireRed_OmniRealism）_2037918131322101761.json、图片生成/图生图/史上最强-小红书动漫转写实真人（FireRed_OmniRealism）_2038424926553640962.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Easy_QwenEdit2509` —— 9/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 9/10 个有
- `Image Comparer (rgthree)` —— 5/10 个有
- `Seed (rgthree)` —— 4/10 个有
- `CR Text` —— 2/10 个有
- `AFL:QwenEditPlusFastuseV2` —— 1/10 个有
- `ImageResizeKJv2` —— 1/10 个有
- `easy int` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 10 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 50% |
| 调度器 | simple | - | 10 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 50%
- 调度器 最常用 simple，10 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
