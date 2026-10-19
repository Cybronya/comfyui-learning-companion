---
name: unknown_workflow_video_lora_sampler_77
type: Unknown Workflow
frequency: 17
level: strong
coverage: 1
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, KSampler, LoadImage, LoraLoader, TeaCache, VAEDecodeTiled, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [视频生成/图生视频/1907272567051444225.json, 视频生成/图生视频/1914851220903686145.json, 视频生成/图生视频/1908884994994151426.json, 视频生成/图生视频/1906686265050247170.json, 视频生成/图生视频/1912469568701329410.json, 视频生成/图生视频/1913534894562078722.json, 视频生成/图生视频/1908140275909468162.json, 视频生成/图生视频/1910308143438491650.json, 视频生成/图生视频/1909579567680684034.json, 视频生成/图生视频/1908472121150812161.json, 视频生成/图生视频/1911952901085036546.json, 视频生成/图生视频/1911801404531638273.json, 视频生成/图生视频/1912077836331511810.json, 视频生成/图生视频/1911646094139555841.json, 视频生成/图生视频/1911792144137318401.json, 视频生成/图生视频/1910201244638740482.json, 视频生成/图生视频/1921368068402921474.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_77

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（视频生成/图生视频/1907272567051444225.json、视频生成/图生视频/1914851220903686145.json、视频生成/图生视频/1908884994994151426.json、视频生成/图生视频/1906686265050247170.json、视频生成/图生视频/1912469568701329410.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `KSampler`
- `LoadImage`
- `LoraLoader`
- `TeaCache`
- `VAEDecodeTiled`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJ` —— 10/17 个有
- `UnetLoaderGGUF` —— 10/17 个有
- `ConcatTextOfUtils` —— 9/17 个有
- `Joy_caption` —— 9/17 个有
- `Joy_caption_load` —— 9/17 个有
- `UNETLoader` —— 7/17 个有
- `Int` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 17 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 17 | 100% |
| 采样算法 | uni_pc | - | 17 | 100% |
| 调度器 | simple | - | 17 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 17 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 17 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 17/17 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，17 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，17 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，17 个样本，一致性 100%
- 调度器 最常用 simple，17 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 高发问题（17/17 个样本）：发现KSampler但没有VAEDecode
