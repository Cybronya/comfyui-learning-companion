---
name: unknown_workflow_lora_sampler_unet_26
type: Unknown Workflow
frequency: 16
level: strong
coverage: 0.912125
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen2511-Edit-动漫转真实照片_2008898951352684545.json, 图片生成/图生图/Qwen_2509_精准设计5_1979461175039660033.json, 图片生成/图生图/Qwen_2509_精准设计之一_1979475260112277505.json, 图片生成/图生图/Qwen_2509_裁剪法换头_1979485624111632385.json, 图片生成/图生图/Qwen_2511_动作编辑LoRA工作流_2008889943266959361.json, 图片生成/图生图/Qwen_Edit_2509一键白膜转材质LoRA_2028629146225610754.json, 图片生成/图生图/Qwen_Edit_2509多角度镜头LoRA_1984448550216089601.json, 图片生成/图生图/Qwen_Edit_2509溶图LoRA_1985259108620189698.json, 图片生成/图生图/Qwen_Edit_2509移除光影LoRA_1988435110183788545.json, 图片生成/图生图/Qwen_Edit_2509精准换头LoRA_1991658276796448770.json, 图片生成/图生图/Qwen_Edit_2509精准镜头控制之二_1991299002844971010.json, 图片生成/图生图/Qwen_Edit_2509重新照明LoRA_1985146456401219586.json, 图片生成/图生图/Qwen_Edit_2509骑在动物身上LoRA_1983328897490153474.json, 图片生成/图生图/人物面部特写和背面角度_2012819282916282369.json, 图片生成/图生图/千问图像编辑2511 双图编辑一致性_2013173412998418434.json, 图片生成/图生图/场景多角度qwen_1990990304591421442.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_26

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/Qwen2511-Edit-动漫转真实照片_2008898951352684545.json、图片生成/图生图/Qwen_2509_精准设计5_1979461175039660033.json、图片生成/图生图/Qwen_2509_精准设计之一_1979475260112277505.json、图片生成/图生图/Qwen_2509_裁剪法换头_1979485624111632385.json、图片生成/图生图/Qwen_2511_动作编辑LoRA工作流_2008889943266959361.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 16 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyLatentImage` —— 15/16 个有
- `PreviewImage` —— 3/16 个有
- `easy imageConcat` —— 3/16 个有
- `FluxKontextMultiReferenceLatentMethod` —— 2/16 个有
- `Int` —— 2/16 个有
- `TextInput_` —— 2/16 个有
- `EmptySD3LatentImage` —— 1/16 个有
- `ImageScale` —— 1/16 个有
- `ImageScaleDownToSize` —— 1/16 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/16 个有
- `RHHiddenNodes` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 16 | 77% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 16 | 100% |
| 采样算法 | euler | - | 16 | 100% |
| 调度器 | simple | - | 16 | 94% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |
| 宽度 | 1024 | 936 - 1664 | 15 | 84% |
| 高度 | 1024 | 720 - 1664 | 15 | 74% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 21/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，16 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，16 个样本，一致性 100%
- 调度器 最常用 simple，16 个样本，一致性 94%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 936 - 1664，15 个样本，取值集中（一致性 84%）
- 高度 中位数 1024，观测区间 720 - 1664，15 个样本
- 高发问题（21/16 个样本）：Steps较低可能导致细节不足
