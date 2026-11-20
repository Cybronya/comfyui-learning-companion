---
name: text_to_image_lora_sampler_clip_169
type: Text To Image
frequency: 10
level: weak
coverage: 0.7765
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, LoraLoaderModelOnly, ResolutionSelector, SaveImage, Text Multiline, UNETLoader, VAEDecode, VAELoader, llama_cpp_instruct_adv, llama_cpp_model_loader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2 文生图工作流_2075455345870327810.json, 图片生成/图生图/Krea2文生图工作流｜人物类特效图生图_2090099072836395010.json, 图片生成/图生图/Krea2灵感创作丨真实感_2099758207337062402.json, 图片生成/图生图/Krea2灵感创作丨真实感_2100393923163283457.json, 图片生成/图生图/Krea2灵感创作丨真实感_2100425518842732545.json, 图片生成/图生图/文生图人物类特效｜Krea2图片生成工作流_2087162836710674433.json, 图片生成/文生图/Kera2 Turbo 4步极速出图｜美少女写实文生图_2098723233347493890.json, 图片生成/文生图/Kera2 Turbo 4步极速出图｜美少女写实文生图_2098731918736056321.json, 图片生成/文生图/Krea2 文生图工作流（Qwen35优化）_2076626681535754241.json, 图片生成/文生图/Krea2经典省心工作流_2073987909992148994.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_169

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Krea2 文生图工作流_2075455345870327810.json、图片生成/图生图/Krea2文生图工作流｜人物类特效图生图_2090099072836395010.json、图片生成/图生图/Krea2灵感创作丨真实感_2099758207337062402.json、图片生成/图生图/Krea2灵感创作丨真实感_2100393923163283457.json、图片生成/图生图/Krea2灵感创作丨真实感_2100425518842732545.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `ResolutionSelector`
- `SaveImage`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 8/10 个有
- `ImpactLogicalOperators` —— 8/10 个有
- `PrimitiveBoolean` —— 8/10 个有
- `easy showAnything` —— 8/10 个有
- `workflow>load image` —— 8/10 个有
- `EmptyImage` —— 5/10 个有
- `JjkText` —— 4/10 个有
- `solarL_SaveImagesToZip` —— 4/10 个有
- `孤海注释` —— 4/10 个有
- `Fast Groups Bypasser (rgthree)` —— 2/10 个有
- `JjkShowText` —— 2/10 个有
- `Text to String` —— 2/10 个有
- `JWInteger` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 80 - 512 | 10 | 38% |
| 高度 | 512 | 80 - 512 | 10 | 38% |
| 采样步数 | 8 | 4 - 8 | 10 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 10 | 29% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | simple | - | 10 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，观测区间 80 - 512，10 个样本，取值分散，一致性仅 38%
- 高度 中位数 512，观测区间 80 - 512，10 个样本，取值分散，一致性仅 38%
- 采样步数 中位数 8，观测区间 4 - 8，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，10 个样本，取值分散，一致性仅 29%
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（14/10 个样本）：Steps较低可能导致细节不足
