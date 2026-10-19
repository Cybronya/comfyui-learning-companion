---
name: text_to_image_lora_sampler_clip_78
type: Text To Image
frequency: 11
level: moderate
coverage: 0.867273
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, EmptyMiniMaxMusic3LatentAudio, JjkText, KSampler, LoraLoaderModelOnly, MiniMaxMusic3TextEncode, SaveAudioAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [音频生成/音频生成/MiniMax Music 3 文生音乐｜一句话生成配乐卡点BGM_2111206982848966658.json, 音频生成/音频生成/MiniMax Music 3 歌曲创作｜音频生成一句话出歌_2096898649795162114.json, 音频生成/音频生成/MiniMax Music 3官方工作流，音频生成AI音乐创作工具_2107240250992062466.json, 音频生成/音频生成/MiniMax Music 3文生歌曲 全节点注释音乐生成工作流_2098735573421879297.json, 音频生成/音频生成/MiniMax Music 3文生音乐，为爱情定制专属情歌音频_2110499128601042946.json, 音频生成/音频生成/MiniMax Music 3音乐生成120秒完整歌曲｜歌词结构标签三段时间音频生成_2089735188401180674.json, 音频生成/音频生成/MiniMax Music 3音乐生成工作流，完整歌曲音频生成工具_2103982727660920834.json, 音频生成/音频生成/MiniMax Music 3音乐生成｜自定义歌曲创作工作流_2095936216268107777.json, 音频生成/音频生成/MiniMax Music3音乐生成｜音频生成_2090430843511721985.json, 音频生成/音频生成/MiniMax Music音乐生成v4｜自动谱曲连接版_2094513516697972737.json, 音频生成/音频生成/MiniMax_Music_3官方工作流，音频生成AI音乐创作工具_2109520599151366145.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_78

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（音频生成/音频生成/MiniMax Music 3 文生音乐｜一句话生成配乐卡点BGM_2111206982848966658.json、音频生成/音频生成/MiniMax Music 3 歌曲创作｜音频生成一句话出歌_2096898649795162114.json、音频生成/音频生成/MiniMax Music 3官方工作流，音频生成AI音乐创作工具_2107240250992062466.json、音频生成/音频生成/MiniMax Music 3文生歌曲 全节点注释音乐生成工作流_2098735573421879297.json、音频生成/音频生成/MiniMax Music 3文生音乐，为爱情定制专属情歌音频_2110499128601042946.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `EmptyMiniMaxMusic3LatentAudio`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `MiniMaxMusic3TextEncode`
- `SaveAudioAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 10/11 个有
- `SeedNode` —— 10/11 个有
- `VAEDecodeAudioTiled` —— 10/11 个有
- `孤海注释` —— 9/11 个有
- `Float` —— 5/11 个有
- `PreviewAudio` —— 4/11 个有
- `CR Text` —— 3/11 个有
- `PrimitiveStringMultiline` —— 3/11 个有
- `MuyeTextEditOutput` —— 2/11 个有
- `PrimitiveBoolean` —— 2/11 个有
- `PrimitiveInt` —— 2/11 个有
- `EmptyImage` —— 1/11 个有
- `JoinStrings` —— 1/11 个有
- `PreviewImage` —— 1/11 个有
- `PrimitiveFloat` —— 1/11 个有
- `RH_LLMAPI_Pro_Node` —— 1/11 个有
- `ShowText|pysssss` —— 1/11 个有
- `SomethingToString` —— 1/11 个有
- `Text` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 5.98626e+14 | 11 | 0% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 11 | 100% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 91% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 80 | 1 - 80 | 11 | 69% |
| 高度 | 80 | 80 - 80 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 5.98626e+14，11 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 91%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 1 - 80，11 个样本
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 风险：采样步数 观测到 5.98626e+14，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 高发问题（10/11 个样本）：Steps较低可能导致细节不足
