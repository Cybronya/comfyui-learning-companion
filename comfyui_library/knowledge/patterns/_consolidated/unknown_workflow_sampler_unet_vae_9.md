---
name: unknown_workflow_sampler_unet_vae_9
type: Unknown Workflow
frequency: 29
level: moderate
coverage: 0.846241
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3多条件参考视频工作流低显存加速版 开源 Ref2VA_2084437517675352065.json, 视频生成/图生视频/MiniMax+H3+参考图图生视频工作流_2084234953285525505.json, 视频生成/图生视频/MiniMax+H3参考生视频6倍加速80GB满配版_2087405259374292993.json, 视频生成/图生视频/MiniMax+H3参考生视频_2084466111193636865.json, 视频生成/图生视频/MiniMax-H3 Ref2va 参考生视频标准版_2095421074551951361.json, 视频生成/图生视频/MiniMax_H3_Fast_2114224611851329538.json, 视频生成/图生视频/Minimax H3 多参生视频_2084365914140659713.json, 视频生成/图生视频/Minimax H3多参视频生成_2084926235125305346.json, 视频生成/图生视频/Minimax H3多图参考视频生成+全节点注释_2099072693512531970.json, 视频生成/图生视频/MinimaxH3开源版参考生视频(8step加速版)_2092363444539453442.json, 视频生成/图生视频/MinimaxH3开源版参考生视频(8step加速版)_2092936286209396737.json, 视频生成/图生视频/MinimaxH3开源版参考生视频(8step加速版)_2094336398261309442.json, 视频生成/图生视频/MinimaxH3开源版参考生视频(8step加速版)_2109218798602641409.json, 视频生成/图生视频/Minimax_H3多图参考视频生成+全节点注释_2099778923717550082.json, 视频生成/图生视频/Minimax_H3多图参考视频生成+全节点注释_2100038725966319618.json, 视频生成/图生视频/minimaxH3多参考视频工作流_2084285648122499073.json, 视频生成/文生视频/MiniMax H3 多模态参考生视频（SageAttention 加速版）_2085990402720616449.json, 视频生成/文生视频/MiniMax H3+ 新4步LoRa + 参考图图生视频工作流_2092505916875829250.json, 视频生成/文生视频/MiniMax H3参考生视频6倍加速24GB通用版_2086411688710066177.json, 视频生成/文生视频/MiniMax H3参考生视频6倍加速48GB高配版_2086459494866968577.json, 视频生成/文生视频/MiniMax H3参考生视频6倍加速80GB满配版_2086411609148313601.json, 视频生成/文生视频/Minimax H3 多模态--综合应用流_2085249742157729793.json, 视频生成/文生视频/Minimax H3多参视频生成+全节点注释_2084873538615472129.json, 视频生成/文生视频/Minimax+H3+Multi-parameter+Reference+Raw+Video_2084191041938345986.json, 视频生成/文生视频/MinimaxH3-全能参考生视频-夏_2093873460580802561.json, 视频生成/文生视频/MinimaxH3开源版 9-3-3参考生视频_2095459758181535745.json, 视频生成/文生视频/minimaxH3多参考视频工作流（超级加速版）_2080928622717784066.json, 视频生成/文生视频/【5】全能多模态--多参视频生成（真正平替seedance）--ref2va模型_2087209584539820034.json, 视频生成/文生视频/海螺MiniMaxH3开源版Turbo 全模式视频整合流_2087092258339385345.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_9

> 由 `engine/knowledge_consolidation` 从 29 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3多条件参考视频工作流低显存加速版 开源 Ref2VA_2084437517675352065.json、视频生成/图生视频/MiniMax+H3+参考图图生视频工作流_2084234953285525505.json、视频生成/图生视频/MiniMax+H3参考生视频6倍加速80GB满配版_2087405259374292993.json、视频生成/图生视频/MiniMax+H3参考生视频_2084466111193636865.json、视频生成/图生视频/MiniMax-H3 Ref2va 参考生视频标准版_2095421074551951361.json…）

- **类型**：Unknown Workflow
- **样本数**：29
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 29 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 28/29 个有
- `PrimitiveFloat` —— 28/29 个有
- `LoadAudio` —— 24/29 个有
- `PrimitiveStringMultiline` —— 20/29 个有
- `PathchSageAttentionKJ` —— 17/29 个有
- `LoadVideo` —— 16/29 个有
- `LoraLoaderModelOnly` —— 15/29 个有
- `EasyCache` —— 14/29 个有
- `GetVideoComponents` —— 13/29 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 11/29 个有
- `CR Prompt Text` —— 8/29 个有
- `VHS_LoadVideo` —— 6/29 个有
- `ImageResizeKJv2` —— 5/29 个有
- `Label (rgthree)` —— 3/29 个有
- `Fast Groups Bypasser (rgthree)` —— 2/29 个有
- `CS-MultiImageLoader` —— 1/29 个有
- `Int` —— 1/29 个有
- `MiniMaxH3ImageToVideo` —— 1/29 个有
- `ModelPreviewOverrideKJ` —— 1/29 个有
- `MuyeTextEditOutput` —— 1/29 个有
- `PlaySound|pysssss` —— 1/29 个有
- `PrimitiveInt` —— 1/29 个有
- `Seed (rgthree)` —— 1/29 个有
- `VHS_LoadAudioUpload` —— 1/29 个有
- `孤海注释` —— 1/29 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
