---
name: unknown_workflow_lora_sampler_clip_23
type: Unknown Workflow
frequency: 13
level: weak
coverage: 0.888462
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SDXLEmptyLatentSizePicker+, SaveImage, Text Multiline, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen文生图极速版QwenQwen_1962119597363236866.json, 图片生成/文生图/多风格绘本_2004518809287491586.json, 图片生成/文生图/文生图千问qwen美女帅哥超清qwen加速版_2008510508328030209.json, 图片生成/文生图/沙雕动漫人物生成—各类动漫和游戏—开高清放大_2024365361033908225.json, 图片生成/文生图/沙雕动漫修仙道具_1975850526229311490.json, 图片生成/文生图/沙雕动漫修仙道具_1977868579548844034.json, 图片生成/文生图/沙雕动漫游戏8090都市人物开高清放大_1960893369214013442.json, 图片生成/文生图/沙雕动漫表情包沙雕动漫超火表情包_1965258449992994817.json, 图片生成/文生图/沙雕动漫都市道具专用工作流_2075022458377293825.json, 图片生成/文生图/沙雕动漫都市道具超清qwen加速版_1960894339947933698.json, 图片生成/文生图/沙雕动画场景-简笔画超清_2024368744855773185.json, 图片生成/文生图/沙雕动画道具—超清加速_2024381279193538562.json, 图片生成/文生图/简笔画都市场景图超清_1965638195176198145.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_23

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/Qwen文生图极速版QwenQwen_1962119597363236866.json、图片生成/文生图/多风格绘本_2004518809287491586.json、图片生成/文生图/文生图千问qwen美女帅哥超清qwen加速版_2008510508328030209.json、图片生成/文生图/沙雕动漫人物生成—各类动漫和游戏—开高清放大_2024365361033908225.json、图片生成/文生图/沙雕动漫修仙道具_1975850526229311490.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SDXLEmptyLatentSizePicker+`
- `SaveImage`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UpscaleModelLoader` —— 12/13 个有
- `ConditioningZeroOut` —— 11/13 个有
- `ImageUpscaleWithModel` —— 10/13 个有
- `easy cleanGpuUsed` —— 10/13 个有
- `easy promptConcat` —— 6/13 个有
- `Anything Everywhere3` —— 5/13 个有
- `CR Text Concatenate` —— 5/13 个有
- `PreviewImage` —— 4/13 个有
- `SaveLatent` —— 4/13 个有
- `UltimateSDUpscale` —— 2/13 个有
- `easy showAnything` —— 2/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024x1024 (1.0) | - | 13 | 62% |
| 高度 | 1 | 1 - 4 | 13 | 35% |
| 采样步数 | 8 | 4 - 15 | 13 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 13 | 35% |
| 采样算法 | euler | - | 13 | 100% |
| 调度器 | simple | - | 13 | 69% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 最常用 1024x1024 (1.0)，13 个样本，一致性 62%
- 高度 中位数 1，观测区间 1 - 4，13 个样本，取值分散，一致性仅 35%
- 采样步数 中位数 8，观测区间 4 - 15，13 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，13 个样本，取值分散，一致性仅 35%
- 采样算法 最常用 euler，13 个样本，一致性 100%
- 调度器 最常用 simple，13 个样本，一致性 69%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（8/13 个样本）：Steps较低可能导致细节不足
