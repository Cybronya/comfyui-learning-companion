---
name: unknown_workflow_sampler_vae_32
type: Unknown Workflow
frequency: 11
level: weak
coverage: 0.959273
common_nodes: [CLIPLoader, KSampler, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/FIBO2_CHAT全能图片G_VGL_优化提示词对比工作流_2114566283193839618.json, 图片生成/文生图/FIBO2_DEV模型50步文生图ComfyUI工作流_2114555974211166209.json, 图片生成/文生图/Nvidia Cosmos Predict2 T2I_1938596846677712898.json, 图片生成/文生图/Ovis文生图工作流_1997584970094952450.json, 图片生成/文生图/QWEN FP8文生图8步快速工作流_1966317820562878466.json, 图片生成/文生图/QWEN官方文生图工作流V1_1968150332159197185.json, 图片生成/文生图/QWen-Image中文渲染-ComfyUI_1952892525439873025.json, 图片生成/文生图/QWen-Image模型lora训练测试工作流_1963484613191749634.json, 图片生成/文生图/QWen2512基础文生图工作流+LoRA_2094427546531229697.json, 图片生成/文生图/Qwen Image 2512文生图_2006571269797453825.json, 图片生成/文生图/Qwen Image 2512（bf16）文生图_2006636107433254914.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_32

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/FIBO2_CHAT全能图片G_VGL_优化提示词对比工作流_2114566283193839618.json、图片生成/文生图/FIBO2_DEV模型50步文生图ComfyUI工作流_2114555974211166209.json、图片生成/文生图/Nvidia Cosmos Predict2 T2I_1938596846677712898.json、图片生成/文生图/Ovis文生图工作流_1997584970094952450.json、图片生成/文生图/QWEN FP8文生图8步快速工作流_1966317820562878466.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 10/11 个有
- `CLIPTextEncode` —— 9/11 个有
- `ModelSamplingAuraFlow` —— 8/11 个有
- `EmptySD3LatentImage` —— 7/11 个有
- `LoraLoaderModelOnly` —— 5/11 个有
- `CFGNorm` —— 2/11 个有
- `CR SDXL Aspect Ratio` —— 2/11 个有
- `Label (rgthree)` —— 2/11 个有
- `TextEncodeFibo2` —— 2/11 个有
- `Anything Everywhere3` —— 1/11 个有
- `CR Prompt Text` —— 1/11 个有
- `Prompts Everywhere` —— 1/11 个有
- `UnetLoaderGGUF` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 50 | 11 | 26% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 5 | 11 | 37% |
| 采样算法 | euler | - | 11 | 82% |
| 调度器 | simple | - | 11 | 73% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 50，11 个样本，取值分散，一致性仅 26%
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 5，11 个样本，取值分散，一致性仅 37%
- 采样算法 最常用 euler，11 个样本，一致性 82%
- 调度器 最常用 simple，11 个样本，一致性 73%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（6/11 个样本）：Steps较低可能导致细节不足
