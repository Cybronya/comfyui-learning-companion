---
name: image_to_image_lora_sampler_unet_75
type: Image To Image
frequency: 8
level: strong
coverage: 0.845
common_nodes: [Anything Everywhere3, CLIPLoader, Int, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ProcessString, RH_LLMAPI_NODE, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy promptLine, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Image-Edit 分镜编辑（Next Scene LoRA）_2005443551607619585.json, 图片生成/图生图/【微电影】镜头风格一致性电影3分镜 Qwen+Next+Scene+影视剧情分镜制作_1980860923768426497.json, 图片生成/图生图/【微电影】镜头风格一致性电影3分镜 Qwen+Next+Scene+影视剧情分镜制作_2010358808517812225.json, 图片生成/图生图/【微电影】镜头风格一致性电影3分镜 Qwen+Next+Scene+影视剧情分镜制作_2016040452352380930.json, 图片生成/图生图/【微电影】镜头风格一致性电影3分镜 Qwen+Next+Scene+影视剧情分镜制作_2075495556738281473.json, 图片生成/图生图/【微电影】镜头风格一致性电影3分镜+Qwen+Next+Scene+影视剧情分镜制作_1999832070736183298.json, 图片生成/图生图/【微电影分镜制作】镜头风格一致性电影分镜 Qwen+Next+Scene_1984487279752265729.json, 图片生成/图生图/一句话出分镜Qwen-Edit-2509影视剧情分镜制作_1985703552763011073.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_75

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Qwen-Image-Edit 分镜编辑（Next Scene LoRA）_2005443551607619585.json、图片生成/图生图/【微电影】镜头风格一致性电影3分镜 Qwen+Next+Scene+影视剧情分镜制作_1980860923768426497.json、图片生成/图生图/【微电影】镜头风格一致性电影3分镜 Qwen+Next+Scene+影视剧情分镜制作_2010358808517812225.json、图片生成/图生图/【微电影】镜头风格一致性电影3分镜 Qwen+Next+Scene+影视剧情分镜制作_2016040452352380930.json、图片生成/图生图/【微电影】镜头风格一致性电影3分镜 Qwen+Next+Scene+影视剧情分镜制作_2075495556738281473.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 8 个 workflow 都包含：
- `Anything Everywhere3`
- `CLIPLoader`
- `Int`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ProcessString`
- `RH_LLMAPI_NODE`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy promptLine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 7/8 个有
- `ShellAgentPluginOutputText` —— 7/8 个有
- `CR Prompt Text` —— 1/8 个有
- `ConditioningZeroOut` —— 1/8 个有
- `Note _O` —— 1/8 个有
- `PreviewImage` —— 1/8 个有
- `PrimitiveStringMultiline` —— 1/8 个有
- `SeedVR2` —— 1/8 个有
- `SeedVR2BlockSwap` —— 1/8 个有
- `SeedVR2ExtraArgs` —— 1/8 个有
- `ttN seed` —— 1/8 个有
- `ttN textOutput` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 8 | 71% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | sa_solver | - | 8 | 88% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，8 个样本，一致性 88%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
