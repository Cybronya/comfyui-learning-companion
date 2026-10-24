---
name: unknown_workflow_lora_sampler_clip_14
type: Unknown Workflow
frequency: 17
level: moderate
coverage: 0.817235
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Int, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/多样性超写实文生图_2052917098942349314.json, 图片生成/文生图/AI电影海报一键生成_2016027708911788033.json, 图片生成/文生图/AI电影海报速成大师_2014963614515470338.json, 图片生成/文生图/Z-image Base+Turbo 双采样 文生图 高级工作流_2041740734788800513.json, 图片生成/文生图/Z-image Base+Turbo 双采样 文生图_2041332481936334850.json, 图片生成/文生图/Z-image base 三阶采样 多样性超写实 文生图_2055553152094621698.json, 图片生成/文生图/ernie turbo + Z-image base+turbo 三阶采样 多样性超写实 文生图 图生图洗图_2044650703913750529.json, 图片生成/文生图/ernie turbo + Z-image base+turbo 三阶采样 多样性超写实 文生图_2051833405628788738.json, 图片生成/文生图/ernie turbo + Z-image base+turbo 三阶采样 多样性超写实 文生图_2052294300981047298.json, 图片生成/文生图/ernie turbo + Z-image base+turbo 三阶采样 多样性超写实 文生图_2052366719192186882.json, 图片生成/文生图/ernie turbo + Z-image base+turbo 三阶采样 多样性超写实 文生图_2052581391463927810.json, 图片生成/文生图/万能图像生成器  文生图  + Z-image base+turbo 三阶采样 多样性_2051125465544437762.json, 图片生成/文生图/三阶采样+多样性超写实+文生图 (1)_2054399447311888386.json, 图片生成/文生图/多样性超写实文生图_2052923543083597826.json, 图片生成/文生图/文生图Z-image base等三阶采样、超真实_2052635800872996865.json, 图片生成/文生图/文生图Z-image+base+_2051840571873996802.json, 图片生成/文生图/超写实文生图ernie turbo + Z-image base+turbo 三种风格任选_2052659897422102530.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_14

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/图生图/多样性超写实文生图_2052917098942349314.json、图片生成/文生图/AI电影海报一键生成_2016027708911788033.json、图片生成/文生图/AI电影海报速成大师_2014963614515470338.json、图片生成/文生图/Z-image Base+Turbo 双采样 文生图 高级工作流_2041740734788800513.json、图片生成/文生图/Z-image Base+Turbo 双采样 文生图_2041332481936334850.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Int`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `RH_LLMAPI_NODE` —— 16/17 个有
- `Text` —— 16/17 个有
- `CR Text` —— 15/17 个有
- `CheckpointLoaderSimple` —— 15/17 个有
- `InversionDemoLazyIndexSwitch` —— 15/17 个有
- `PreviewImage` —— 15/17 个有
- `RH_LLMAPI_Pro_Node` —— 15/17 个有
- `VAEEncode` —— 15/17 个有
- `ImpactSwitch` —— 2/17 个有
- `LatentFrequencyEnhancer_lrzjason` —— 2/17 个有
- `LayerFilter: HDREffects` —— 2/17 个有
- `AILab_QwenVL` —— 1/17 个有
- `LoadImage` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 17 | 100% |
| Prompt 约束强度(CFG) | 8 | 3 - 15 | 17 | 60% |
| 采样算法 | 1 | 1 - 1 | 17 | 100% |
| 调度器 | euler | - | 17 | 100% |
| 重绘幅度 | simple | - | 17 | 100% |
| 宽度 | 960 | 512 - 1536 | 17 | 78% |
| 高度 | 1536 | 512 - 1536 | 17 | 75% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，17 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 3 - 15，17 个样本
- 采样算法 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，17 个样本，一致性 100%
- 重绘幅度 最常用 simple，17 个样本，一致性 100%
- 宽度 中位数 960，观测区间 512 - 1536，17 个样本
- 高度 中位数 1536，观测区间 512 - 1536，17 个样本
- 风险：Prompt 约束强度(CFG) 观测到 15，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
