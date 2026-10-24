---
name: unknown_workflow_sampler_unet_vae_168
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.77
common_nodes: [CFGNorm, CLIPLoader, EmptySD3LatentImage, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen_Imgae_Edit任意产品纹理提取与纹理迁移工作流_2067425870721142786.json, 图片生成/图生图/Qwen_Imgae_Edit任意产品纹理提取与纹理迁移工作流_2067511850530594818.json, 图片生成/图生图/印花提取-Qwen-Edit-2511(快速)，测试_2044644254810644481.json, 图片生成/图生图/印花提取-Qwen-Edit-2511-V2_2041179666408546306.json, 图片生成/文生图/服装_床品_地毯花纹一键提取！QwenImageEdit2511工作流详解，小白友好+全节点注释_2059565759478718465.json, 图片生成/文生图/设计师必备ComfyUI工作流：实物照片→干净印花，全节点手把手注释_2059565790445260801.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_168

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Qwen_Imgae_Edit任意产品纹理提取与纹理迁移工作流_2067425870721142786.json、图片生成/图生图/Qwen_Imgae_Edit任意产品纹理提取与纹理迁移工作流_2067511850530594818.json、图片生成/图生图/印花提取-Qwen-Edit-2511(快速)，测试_2044644254810644481.json、图片生成/图生图/印花提取-Qwen-Edit-2511-V2_2041179666408546306.json、图片生成/文生图/服装_床品_地毯花纹一键提取！QwenImageEdit2511工作流详解，小白友好+全节点注释_2059565759478718465.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `EmptySD3LatentImage`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 4/6 个有
- `LoraLoader` —— 4/6 个有
- `CR SDXL Aspect Ratio` —— 2/6 个有
- `CR Text` —— 2/6 个有
- `CR Text Concatenate` —— 2/6 个有
- `ImpactInt` —— 2/6 个有
- `LayerColor: AutoAdjustV2` —— 2/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/6 个有
- `LoraLoaderModelOnly` —— 2/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 6 - 8 | 6 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| LoRA 模型强度 | 1.25 | 1 - 1.5 | 4 | 80% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 6 - 8，6 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1.25，观测区间 1 - 1.5，4 个样本，取值集中（一致性 80%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（8/6 个样本）：Steps较低可能导致细节不足
