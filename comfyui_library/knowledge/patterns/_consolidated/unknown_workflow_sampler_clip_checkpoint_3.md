---
name: unknown_workflow_sampler_clip_checkpoint_3
type: Unknown Workflow
frequency: 9
level: weak
coverage: 0.965111
common_nodes: [CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentAudio, KSampler, SaveAudio, VAEDecodeAudio]
problems: [发现KSampler但没有VAEDecode, Steps较低可能导致细节不足]
missing: []
members: [音频生成/音频生成/Stable Audio Open 文生音频音效声音生成_2041681190037491713.json, 音频生成/音频生成/Stable-audio纯音乐生成_1989534377547845633.json, 音频生成/音频生成/stable-audio -medium-长背景音乐生成_2058890267595460610.json, 音频生成/音频生成/stable-audio-效音生成_2058888194803982337.json, 音频生成/音频生成/stable-audio-背景音乐生成_2058396093842542593.json, 音频生成/音频生成/强大的文字生音频_音效 stable-audio-open_1911590798788624386.json, 音频生成/音频生成/强大的音效生成器 stable-audio_1937725826492469249.json, 音频生成/音频生成/文字生音频_音效 stable-audio-open_1834600696275693569.json, 音频生成/音频生成/文字生音频_音效_2007400748958617601.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_checkpoint_3

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（音频生成/音频生成/Stable Audio Open 文生音频音效声音生成_2041681190037491713.json、音频生成/音频生成/Stable-audio纯音乐生成_1989534377547845633.json、音频生成/音频生成/stable-audio -medium-长背景音乐生成_2058890267595460610.json、音频生成/音频生成/stable-audio-效音生成_2058888194803982337.json、音频生成/音频生成/stable-audio-背景音乐生成_2058396093842542593.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentAudio`
- `KSampler`
- `SaveAudio`
- `VAEDecodeAudio`

**可变部分**（部分 workflow 才有）：
- `PreviewAudio` —— 5/9 个有
- `DeepTranslatorTextNode` —— 4/9 个有
- `PrimitiveFloat` —— 2/9 个有
- `RH_Translator` —— 2/9 个有
- `NumberClamp` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 60 | 8 - 60 | 9 | 42% |
| Prompt 约束强度(CFG) | 7 | 1 - 7 | 9 | 43% |
| 采样算法 | dpmpp_3m_sde_gpu | - | 9 | 67% |
| 调度器 | exponential | - | 9 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 40 | 10 - 380 | 8 | 0% |
| 高度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 9/9 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |
| Steps较低可能导致细节不足 | 3/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 60，观测区间 8 - 60，9 个样本，取值分散，一致性仅 42%
- Prompt 约束强度(CFG) 中位数 7，观测区间 1 - 7，9 个样本，取值分散，一致性仅 43%
- 采样算法 最常用 dpmpp_3m_sde_gpu，9 个样本，一致性 67%
- 调度器 最常用 exponential，9 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 40，观测区间 10 - 380，8 个样本，取值分散，一致性仅 0%
- 高度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：发现KSampler但没有VAEDecode
