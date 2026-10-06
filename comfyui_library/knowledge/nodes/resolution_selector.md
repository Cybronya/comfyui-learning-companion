# ResolutionSelector

## 节点类型

`ResolutionSelector`

## 分类

Latent Generation（辅助选参）

## 作用

用下拉框选宽高比 + 倍率，输出对应的宽度/高度数值，替代手填分辨率。
常与 `EmptyLatentImage` / EmptySD3Latent 类节点串联。

## 参数（统计自 404 个真实 workflow，179 次出现）

| 参数 | 说明 | 实测分布 |
|---|---|---|
| resolution | 目标宽高比 | 9:16 竖屏 72 / 16:9 横屏 61 / 3:4 19 / 2:3 17 / 1:1 5 |
| multiplier | 分辨率倍率 | 2 与 2.2 最常见（基准 1024 → 2048 级别） |
| divisible_by | 取整步长 | 32 为主，部分 8 |

## 常见问题与风险

- multiplier 过大（≥3）在低显存下容易 OOM；竖屏 9:16 比 1:1 更吃显存。
- divisible_by 与下游放大节点的步长不一致时会报尺寸错误。

## 可信度

Generated（2026-10-06，参数分布实测，行为描述为通行语义）TODO(待验证)
