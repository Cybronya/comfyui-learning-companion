---
name: unknown_workflow_sampler_unet_vae_5
type: Unknown Workflow
frequency: 31
level: moderate
coverage: 0.487677
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/AI代码侠土豆-MiniMax H3 T2V（文生视频）_2084169620658937858.json, 视频生成/图生视频/GF02-MiniMax H3图生视频_2084710216851087361.json, 视频生成/图生视频/H3 Ref2VA 多图综合参考 - 87time_2084503529204576258.json, 视频生成/图生视频/H3 动漫转真人+ 指定人物_2093180746625273857.json, 视频生成/图生视频/H3_动作迁移 + 深度视频参考_2090034137221648385.json, 视频生成/图生视频/H3动作迁移！9分钟可出视频！_2103098076767543298.json, 视频生成/图生视频/H3最强二采【唐僧彩蛋】_2107659032340287490.json, 视频生成/图生视频/H3最强二采【飓风京剧】_2107672314556010498.json, 视频生成/图生视频/H3最强二采，吊打SelfLift【虚空折叠流】_2107371063817621505.json, 视频生成/图生视频/H3最强二采，音画俱佳_2107833447233441793.json, 视频生成/图生视频/H3最强全能工作流之言出法随_2100506302412840961.json, 视频生成/图生视频/H3最强全能工作流之言出法随_2101855618586988546.json, 视频生成/图生视频/H3最强全能工作流之言出法随_2102665425023750145.json, 视频生成/图生视频/H3最强动作工作流-真武大弟篇【金鱼佬框架--吃猪侠定制版】_2098093642488565761.json, 视频生成/图生视频/H3最强双采FL2-736P高清PRO-焚诀展开篇_2101855011373404161.json, 视频生成/图生视频/H3最强双采FL2-736P高清PRO-焚诀展开篇_2102664968234692610.json, 视频生成/图生视频/H3超强工作流_2107296344921698306.json, 视频生成/图生视频/MMH3全能参考生视频自用调优版（附带视频续接教程）_2096409310929702913.json, 视频生成/图生视频/MiniMax H3-图生视频_2103135562264834050.json, 视频生成/图生视频/MiniMax H3-多参考生视频-优化版_2108223200814518274.json, 视频生成/图生视频/MiniMax H3-多参考生视频-优化版_2108234638559899650.json, 视频生成/图生视频/MiniMax H3-多参考生视频-去油王版_2094419718181572610.json, 视频生成/图生视频/MiniMax H3-多参考生视频-去油王版_2111461486425100290.json, 视频生成/图生视频/MiniMax+H3-多参考生视频（9图片+3视频+3音频）_2101587742454009857.json, 视频生成/图生视频/MiniMax+H3-多参考生视频（9图片+3视频+3音频）二采_2109901185510629378.json, 视频生成/图生视频/MiniMax_H3-多参考7P3A2V生视频-二采优化版_2100561807021797378.json, 视频生成/图生视频/MiniMax_H3-多参考7P3A2V生视频-优化版_2100555142960603138.json, 视频生成/图生视频/进阶版！MiniMax H3 Ref2VA 多参生视频工作流_2102256455968710658.json, 视频生成/图生视频/（最强一致性Singularity_v2）Minimax_H3多参考双采生视频_2113793684742434817.json, 视频生成/图生视频/（最强一致性Singularity）Minimax H3多参考双采生视频_2097875587942666242.json, 视频生成/图生视频/（最强一致性Singularity）Minimax H3多参考双采生视频多比例版本_2104119164674859010.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_5

> 由 `engine/knowledge_consolidation` 从 31 个 workflow 归纳得出（视频生成/图生视频/AI代码侠土豆-MiniMax H3 T2V（文生视频）_2084169620658937858.json、视频生成/图生视频/GF02-MiniMax H3图生视频_2084710216851087361.json、视频生成/图生视频/H3 Ref2VA 多图综合参考 - 87time_2084503529204576258.json、视频生成/图生视频/H3 动漫转真人+ 指定人物_2093180746625273857.json、视频生成/图生视频/H3_动作迁移 + 深度视频参考_2090034137221648385.json…）

- **类型**：Unknown Workflow
- **样本数**：31
- **可信度**：中等可信
- **平均知识覆盖**：49%

## 共有节点

全部 31 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 30/31 个有
- `ResolutionSelector` —— 30/31 个有
- `Text` —— 30/31 个有
- `MiniMaxH3ReferenceToVideo` —— 29/31 个有
- `VHS_VideoCombine` —— 29/31 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 28/31 个有
- `GetNode` —— 27/31 个有
- `LTXVConcatAVLatent` —— 27/31 个有
- `LTXVSeparateAVLatent` —— 27/31 个有
- `MinimaxH3LatentUpscaler3D` —— 27/31 个有
- `SetNode` —— 27/31 个有
- `SplitSigmas` —— 26/31 个有
- `VHS_LoadVideo` —— 26/31 个有
- `easy float` —— 26/31 个有
- `LoadAudio` —— 25/31 个有
- `LoraLoaderModelOnly` —— 25/31 个有
- `忽略多组孤海` —— 24/31 个有
- `Label (rgthree)` —— 8/31 个有
- `EmptyImage` —— 5/31 个有
- `孤海注释` —— 5/31 个有
- `PreviewImage` —— 4/31 个有
- `CreateVideo` —— 3/31 个有
- `Lora Loader Stack (rgthree)` —— 3/31 个有
- `ModelAttentionBackend` —— 3/31 个有
- `SolAttnMiniMax` —— 3/31 个有
- `MiniMaxH3ImageToVideo` —— 2/31 个有
- `PlaySound|pysssss` —— 2/31 个有
- `SaveVideo` —— 2/31 个有
- `CR Text` —— 1/31 个有
- `CR Text Concatenate` —— 1/31 个有
- `Fast Groups Bypasser (rgthree)` —— 1/31 个有
- `ImageScale` —— 1/31 个有
- `ModelPreviewOverrideKJ` —— 1/31 个有
- `easy cleanGpuUsed` —— 1/31 个有
- `easy int` —— 1/31 个有
- `easy showAnything` —— 1/31 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
