---
name: unknown_workflow_sampler_clip_unet_80
type: Unknown Workflow
frequency: 12
level: weak
coverage: 0.910583
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/2030261410919354369.json, 图片生成/文生图/90后动漫风格-ZImage文生图_2018945323267268610.json, 图片生成/文生图/Flow-DPO LoRA工作流：AI人像终于不像塑料了！这个LoRA让光照秒变真实✨_2028104630768504833.json, 图片生成/文生图/Flow-DPO LoRA工作流：AI人像终于不像塑料了！这张照片太真实了_2028835652560756738.json, 图片生成/文生图/Qwen-Image-2512-Wuli_2007448165187854338.json, 图片生成/文生图/Qwen-Image-2512-lightx2v_2007448158065922050.json, 图片生成/文生图/Qwen-Image-2512文生图大模型：人物更真实、毛发更自然、文字排版更准确！_2006620335499644929.json, 图片生成/文生图/Z-Image-Turbo文生图（OpenClaw远程控制版本）_2020379259021303809.json, 图片生成/文生图/Z-Image_1998633899876057090.json, 图片生成/文生图/Z-Image动漫加强，简单实用_2002386827807997953.json, 图片生成/文生图/Z-Image动漫加强，简单实用_2005662325996744706.json, 图片生成/文生图/Z-Image动漫加强，简单实用（人脸多样性增强）_2006603694439141377.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_80

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/2030261410919354369.json、图片生成/文生图/90后动漫风格-ZImage文生图_2018945323267268610.json、图片生成/文生图/Flow-DPO LoRA工作流：AI人像终于不像塑料了！这个LoRA让光照秒变真实✨_2028104630768504833.json、图片生成/文生图/Flow-DPO LoRA工作流：AI人像终于不像塑料了！这张照片太真实了_2028835652560756738.json、图片生成/文生图/Qwen-Image-2512-Wuli_2007448165187854338.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 11/12 个有
- `ConditioningZeroOut` —— 8/12 个有
- `ModelSamplingAuraFlow` —— 8/12 个有
- `PrimitiveStringMultiline` —— 6/12 个有
- `Label (rgthree)` —— 4/12 个有
- `easy int` —— 4/12 个有
- `easy promptConcat` —— 3/12 个有
- `easy seed` —— 3/12 个有
- `Image Comparer (rgthree)` —— 1/12 个有
- `MuyeTextEditOutput` —— 1/12 个有
- `StringFunction|pysssss` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 50 | 12 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 12 | 34% |
| 采样算法 | euler | - | 12 | 58% |
| 调度器 | simple | - | 12 | 92% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 50，12 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，12 个样本，取值分散，一致性仅 34%
- 采样算法 最常用 euler，12 个样本，一致性 58%
- 调度器 最常用 simple，12 个样本，一致性 92%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（12/12 个样本）：Steps较低可能导致细节不足
